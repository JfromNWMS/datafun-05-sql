SELECT a.last_name, b.title FROM books b
JOIN authors a ON b.author_id = a.author_id
WHERE a.last_name LIKE 'a%'
   OR a.last_name LIKE 'e%'
   OR a.last_name LIKE 'i%'
   OR a.last_name LIKE 'o%'
   OR a.last_name LIKE 'u%'
GROUP BY a.last_name, b.title;