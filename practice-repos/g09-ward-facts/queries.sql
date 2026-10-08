-- Q1: total population
SELECT SUM(population) AS total_population FROM wards;
-- Q2: the largest ward
SELECT ward_name, population FROM wards ORDER BY population DESC LIMIT 1;
