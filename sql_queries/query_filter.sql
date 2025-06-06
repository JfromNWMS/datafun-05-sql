SELECT a.last_name, b.title
FROM authors a
LEFT JOIN books b ON a.author_id = b.author_id
WHERE a.author_id LIKE '%2%';