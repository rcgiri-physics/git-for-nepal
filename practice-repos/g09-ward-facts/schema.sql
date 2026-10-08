-- Portable SQL (works in MySQL and SQLite).
DROP TABLE IF EXISTS wards;
CREATE TABLE wards (
  ward_id INTEGER PRIMARY KEY,
  ward_name VARCHAR(50) NOT NULL,
  population INTEGER NOT NULL,
  households INTEGER NOT NULL
);
INSERT INTO wards VALUES (1, 'Test Ward One', 820, 170);
INSERT INTO wards VALUES (2, 'Test Ward Two', 1450, 310);
INSERT INTO wards VALUES (3, 'Test Ward Three', 990, 205);
INSERT INTO wards VALUES (4, 'Test Ward Four', 2310, 480);
INSERT INTO wards VALUES (5, 'Test Ward Five', 640, 140);
