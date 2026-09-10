-- 1. Content type distribution
SELECT content_type, COUNT(*) total FROM contents GROUP BY content_type ORDER BY total DESC;

-- 2. Content additions by year
SELECT EXTRACT(YEAR FROM date_added) year_added, COUNT(*) titles
FROM contents WHERE date_added IS NOT NULL
GROUP BY year_added ORDER BY year_added;

-- 3. Top 10 countries
SELECT country_name, COUNT(*) titles
FROM content_countries cc JOIN countries c USING(country_id)
GROUP BY country_name ORDER BY titles DESC LIMIT 10;

-- 4. Top 10 genres
SELECT genre_name, COUNT(*) titles
FROM content_genres cg JOIN genres g USING(genre_id)
GROUP BY genre_name ORDER BY titles DESC LIMIT 10;

-- 5. Average movie duration
SELECT ROUND(AVG(duration_value),2) avg_minutes
FROM contents WHERE content_type='Movie' AND duration_unit='min';

-- 6. Maturity category
SELECT maturity_category, COUNT(*) titles
FROM contents GROUP BY maturity_category ORDER BY titles DESC;

-- 7. Release year trend
SELECT release_year, COUNT(*) titles
FROM contents GROUP BY release_year ORDER BY release_year;

-- 8. Oldest and newest content
SELECT MIN(release_year) oldest, MAX(release_year) newest FROM contents;

-- 9. Rating by content type
SELECT content_type, rating, COUNT(*) titles
FROM contents GROUP BY content_type, rating ORDER BY content_type, titles DESC;

-- 10. Countries with movies
SELECT c.country_name, COUNT(*) movies
FROM content_countries cc JOIN countries c USING(country_id)
JOIN contents ct ON ct.content_id=cc.content_id
WHERE ct.content_type='Movie'
GROUP BY c.country_name ORDER BY movies DESC;

-- 11. Countries with TV Shows
SELECT c.country_name, COUNT(*) shows
FROM content_countries cc JOIN countries c USING(country_id)
JOIN contents ct ON ct.content_id=cc.content_id
WHERE ct.content_type='TV Show'
GROUP BY c.country_name ORDER BY shows DESC;

-- 12. Genre by content type
SELECT ct.content_type, g.genre_name, COUNT(*) titles
FROM content_genres cg JOIN genres g USING(genre_id)
JOIN contents ct ON ct.content_id=cg.content_id
GROUP BY ct.content_type, g.genre_name
ORDER BY ct.content_type, titles DESC;

-- 13. Recent content
SELECT title, release_year, rating
FROM contents ORDER BY release_year DESC LIMIT 10;

-- 14. Adult content percentage
SELECT ROUND(100.0 * COUNT(*) FILTER (WHERE maturity_category='Adult') / COUNT(*),2) adult_percentage
FROM contents;

-- 15. Average content age by type
SELECT content_type, ROUND(AVG(content_age),2) avg_content_age
FROM contents GROUP BY content_type;
