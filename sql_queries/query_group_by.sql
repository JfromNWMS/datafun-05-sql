SELECT a.last, b.title, b.year_published
FROM authors a
LEFT JOIN books b ON a.author_id = b.author_id
WHERE a.author_id LIKE '%2%';