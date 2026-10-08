# Forgejo on a school LAN (tier 2)

> **Untested on hardware.** The compose file is a starting point written from Forgejo's documented container usage; check the current Forgejo docs for the latest image tag and options before relying on it. A Raspberry Pi 4-class board is the intended minimum — verify before the Grade 9 pilot.

## Setup
1. Install Docker and the compose plugin on the server PC.
2. Edit `docker-compose.yml`: set `ROOT_URL` to the server's LAN address (e.g. `http://192.168.1.10:3000/`) and pin the image tag.
3. `docker compose up -d`, open `http://<server>:3000`, finish the install page (choose SQLite).
4. Create a **private organisation** per class. The teacher creates student accounts with pseudonymous usernames (`student07`), no real email.
5. Students clone with `git clone http://<server>:3000/class-9a/ward-facts.git`.

## Backups
Copy the `./forgejo-data` folder to a USB stick weekly.

## Safety
- No internet exposure; do not port-forward the server.
- Use HTTP only on the LAN; do not reuse real passwords.
