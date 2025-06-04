SELECT a.last, MAX(b.year_published) AS year_published
FROM authors a
LEFT JOIN books b ON a.author_id = b.author_id
GROUP BY a.last
ORDER BY year_published DESC;