#!/usr/bin/env python3
"""Build the printable book (PDF) from the Markdown lessons.

    python tools/build_book.py            # writes book/dist/git-for-nepal-book.pdf
    python tools/build_book.py --html     # only writes book/dist/book.html

Steps: read book/book.yml -> render each Markdown file with the same extensions as
mkdocs.yml -> rewrite links (in-book links become page anchors, other site pages become
website URLs) -> print with headless Chrome/Edge -> read the PDF's named destinations to
learn each chapter's page -> print again with page numbers in the table of contents ->
add PDF bookmarks and metadata with pypdf.

Needs: markdown, pymdown-extensions, pyyaml, pypdf, and Chrome, Chromium or Edge
(set CHROME=/path/to/browser if it is not found automatically).
"""
import html
import os
import pathlib
import posixpath
import re
import shutil
import subprocess
import sys
import tempfile

import markdown
import yaml
from pypdf import PdfReader, PdfWriter

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs" / "en"
BOOK = ROOT / "book"
FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)
EXTENSIONS = ["admonition", "tables", "toc", "attr_list", "pymdownx.details", "pymdownx.superfences"]


def slug_for(path):
    return "ch-" + re.sub(r"[^a-z0-9]+", "-", path.lower().removesuffix(".md")).strip("-")


def find_browser():
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    ]
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "microsoft-edge"):
        found = shutil.which(name)
        if found:
            candidates.insert(0, found)
    for c in candidates:
        if pathlib.Path(c).exists():
            return c
    sys.exit("No Chrome/Chromium/Edge found; set the CHROME environment variable.")


def load_manifest():
    data = yaml.safe_load((BOOK / "book.yml").read_text(encoding="utf-8"))
    entries = []  # (kind, part_index, dict)

    def norm(item):
        return item if isinstance(item, dict) else {"path": item}

    for item in data.get("front", []):
        entries.append(("front", None, norm(item)))
    for i, part in enumerate(data["parts"]):
        entries.append(("part", i, {"title": part["title"]}))
        for item in part["chapters"]:
            entries.append(("chapter", i, norm(item)))
    return data, entries


def chapter_kind(fm):
    if not fm or "grade" not in fm:
        return ""
    m = re.match(r"g\d+-m(\d+)", str(fm.get("id", "")))
    module = f" · Module {int(m.group(1))}" if m else ""
    hours = fm.get("hours")
    periods = f" · {hours} period{'s' if hours != 1 else ''}" if hours else ""
    tiers = fm.get("tier_support")
    tier = f" · Tiers {', '.join(map(str, tiers))}" if tiers else ""
    return f"Grade {fm['grade']}{module}{periods}{tier}"


def rewrite(html_text, path, slug, in_book, site_url):
    """Prefix ids with the chapter slug and turn links into in-book anchors or URLs."""
    here = posixpath.dirname(path)

    html_text = re.sub(r'id="([^"]+)"', lambda m: f'id="{slug}--{m.group(1)}"', html_text)

    def fix_href(m):
        attrs_before, href, attrs_after, text = m.group(1), html.unescape(m.group(2)), m.group(3), m.group(4)
        if href.startswith("#"):
            return f'<a{attrs_before}href="#{slug}--{href[1:]}"{attrs_after}>{text}</a>'
        if re.match(r"^(https?:|mailto:)", href):
            plain = re.sub(r"<[^>]+>", "", text).strip()
            if plain.rstrip("/") == href.rstrip("/") or href.startswith("mailto:"):
                return m.group(0)
            return f'<a{attrs_before}href="{html.escape(href)}" class="ext" data-url="{html.escape(href)}"{attrs_after}>{text}</a>'
        target, _, anchor = href.partition("#")
        resolved = posixpath.normpath(posixpath.join(here, target)) if target else path
        if resolved in in_book:
            t = in_book[resolved]
            dest = f"#{t}--{anchor}" if anchor else f"#{t}"
            return f'<a{attrs_before}href="{dest}"{attrs_after}>{text}</a>'
        if resolved.endswith(".md"):
            page = resolved.removesuffix(".md")
            page = page.removesuffix("index").rstrip("/")
            url = site_url + (page + "/" if page else "") + (f"#{anchor}" if anchor else "")
        else:
            url = site_url + resolved
        return f'<a{attrs_before}href="{html.escape(url)}" class="ext" data-url="{html.escape(url)}"{attrs_after}>{text}</a>'

    html_text = re.sub(r'<a([^>]*?)href="([^"]*)"([^>]*)>(.*?)</a>', fix_href, html_text, flags=re.S)
    # "- [ ] item" checklists -> printable boxes
    html_text = re.sub(r"<li>\s*\[[ xX]\]\s*", '<li class="task">', html_text)
    return html_text


def render_chapter(item, in_book, site_url):
    path = item["path"]
    text = (DOCS / path).read_text(encoding="utf-8")
    fm = {}
    m = FM.match(text)
    if m:
        fm = yaml.safe_load(m.group(1)) or {}
        text = text[m.end():]
    body = markdown.markdown(text, extensions=EXTENSIONS, extension_configs={"toc": {"permalink": False}})
    slug = in_book[path]
    body = rewrite(body, path, slug, in_book, site_url)
    title_m = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
    title = item.get("title") or (re.sub(r"<[^>]+>", "", title_m.group(1)).strip() if title_m else path)
    if item.get("title") and title_m:
        body = body.replace(title_m.group(0), f'<h1 id="{slug}--title">{html.escape(title)}</h1>', 1)
    kind = chapter_kind(fm)
    kind_html = f'<div class="chapter-kind">{html.escape(kind)}</div>' if kind else ""
    level = item.get("level", 1)
    section = f'<section class="chapter level{level}" id="{slug}">{kind_html}{body}</section>'
    return title, level, section


def build_html(data, entries, pages=None):
    site_url = data["site_url"]
    in_book = {e[2]["path"]: slug_for(e[2]["path"]) for e in entries if e[0] in ("front", "chapter")}
    toc, sections, outline = [], [], []
    for kind, part_i, item in entries:
        if kind == "part":
            pid = f"part-{part_i + 1}"
            title = item["title"]
            sections.append(f'<section class="divider" id="{pid}"><h1>{html.escape(title)}</h1><div class="rule"></div></section>')
            toc.append(("part", pid, title))
            outline.append((0, pid, title))
            continue
        title, level, section = render_chapter(item, in_book, site_url)
        sid = in_book[item["path"]]
        sections.append(section)
        cls = "ch" if level == 1 else "ch2"
        toc.append((cls, sid, title))
        outline.append((level, sid, title))

    def pn(i):
        return str(pages[i] + 1) if pages and i in pages else "000"

    toc_html = "".join(
        f'<li class="{cls}"><a href="#{i}">{html.escape(t)}</a><span class="dots"></span><span class="pn">{pn(i)}</span></li>'
        for cls, i, t in toc
    )
    css = (BOOK / "print.css").read_text(encoding="utf-8")
    graph = "o---o---o---o---o  main\n         \\       /\n          o---o-'    feature"
    cover = f"""
<section class="cover" id="cover">
  <div class="series">{html.escape(data['series'])}</div>
  <h1>{html.escape(data['title'])}</h1>
  <div class="subtitle">{html.escape(data['subtitle'])}</div>
  <div class="graph">{html.escape(graph)}</div>
  <div class="np">नेपालका लागि Git — संस्करण नियन्त्रण, कक्षा ८–१२</div>
  <div class="bottom">{html.escape(data['authors'])}<br>{html.escape(data['edition'])}<br>{html.escape(data['licence'])}</div>
</section>
<section class="verso">
  <p><strong>{html.escape(data['title'])}: {html.escape(data['subtitle'])}</strong></p>
  <p>{html.escape(data['edition'])}. Grades 9–12 are unpiloted drafts.</p>
  <p>© {html.escape(data['authors'])}. Text licensed under Creative Commons Attribution 4.0 International (CC BY 4.0); code and templates under the MIT License.
  You may copy, print, adapt and share this book, including commercially, with credit:</p>
  <p>“Git for Nepal” by Ram Chandra Giri and contributors, licensed under CC BY 4.0. Source: {html.escape(data['repo_url'])}</p>
  <p><a href="#toc">Contents</a> · Website: {html.escape(site_url)}. Third-party resources keep their own licences and are linked, not copied, unless their licence allows it.</p>
</section>
<section class="toc" id="toc"><h1>Contents</h1><ol>{toc_html}</ol></section>"""
    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{html.escape(data['title'])}</title>
<style>{css}</style></head><body>{cover}{''.join(sections)}</body></html>"""
    return doc, outline


def print_pdf(browser, html_path, pdf_path):
    with tempfile.TemporaryDirectory() as profile:
        cmd = [browser, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
               f"--user-data-dir={profile}", f"--print-to-pdf={pdf_path}", html_path.resolve().as_uri()]
        subprocess.run(cmd, check=True, capture_output=True, timeout=600)
    if not pathlib.Path(pdf_path).exists():
        sys.exit("The browser did not write the PDF.")


def destination_pages(pdf_path):
    reader = PdfReader(pdf_path)
    index = {p.indirect_reference.idnum: i for i, p in enumerate(reader.pages)}
    dests = reader.trailer["/Root"].get("/Dests")
    pages = {}
    if dests:
        for name, value in dests.get_object().items():
            arr = value.get_object()
            if isinstance(arr, dict):
                arr = arr["/D"]
            pages[name.lstrip("/")] = index.get(arr[0].idnum)
    return pages, len(reader.pages)


def finish(pdf_in, pdf_out, data, outline, pages):
    reader = PdfReader(pdf_in)
    writer = PdfWriter()
    writer.append(reader)
    writer.add_metadata({"/Title": f"{data['title']}: {data['subtitle']}", "/Author": data["authors"],
                         "/Subject": "Version control (Git) curriculum, Grades 8-12", "/Keywords": "Git, version control, Nepal, curriculum"})
    if "toc" in pages:
        writer.add_outline_item("Contents", pages["toc"])
    parent = None
    for level, sid, title in outline:
        if sid not in pages or pages[sid] is None:
            continue
        if level == 0:
            parent = writer.add_outline_item(title, pages[sid])
        else:
            writer.add_outline_item(title, pages[sid], parent=parent)
    writer.page_mode = "/UseOutlines"
    with open(pdf_out, "wb") as f:
        writer.write(f)


def main():
    data, entries = load_manifest()
    out_pdf = ROOT / data["output"]
    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    html_path = out_pdf.parent / "book.html"

    doc, outline = build_html(data, entries)
    html_path.write_text(doc, encoding="utf-8")
    if "--html" in sys.argv:
        print(f"wrote {html_path.relative_to(ROOT)}")
        return

    browser = find_browser()
    with tempfile.TemporaryDirectory() as tmp:
        first = pathlib.Path(tmp) / "pass1.pdf"
        print_pdf(browser, html_path, first)
        pages, n1 = destination_pages(first)

        doc, outline = build_html(data, entries, pages)
        html_path.write_text(doc, encoding="utf-8")
        second = pathlib.Path(tmp) / "pass2.pdf"
        print_pdf(browser, html_path, second)
        pages2, n2 = destination_pages(second)
        moved = [k for k, v in pages.items() if k.startswith(("ch-", "part-")) and pages2.get(k) != v]
        if moved:
            print(f"warning: {len(moved)} chapters moved between passes (e.g. {moved[:3]})")
        finish(second, out_pdf, data, outline, pages2)
    missing = [sid for _, sid, _ in outline if sid not in pages2]
    if missing:
        print(f"warning: no page found for {missing}")
    size = out_pdf.stat().st_size / 1e6
    print(f"wrote {out_pdf.relative_to(ROOT)}: {n2} pages, {size:.1f} MB")


if __name__ == "__main__":
    main()
