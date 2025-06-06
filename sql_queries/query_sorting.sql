SELECT a.last_name, MAX(b.year_published) AS last_year_published
FROM authors a
LEFT JOIN books b ON a.author_id = b.author_id
GROUP BY a.last_name
ORDER BY last_year_published DESC;