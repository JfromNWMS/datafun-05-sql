SELECT DISTINCT a.first_name, a.last_name, b.title, b.year_published
FROM authors a
INNER JOIN books b ON a.author_id = b.author_id
ORDER BY b.title ASC;