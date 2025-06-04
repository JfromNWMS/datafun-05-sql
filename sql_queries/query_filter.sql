SELECT a.last, b.title FROM books b
JOIN authors a ON b.author_id = a.author_id
WHERE a.last LIKE 'a%'
   OR a.last LIKE 'e%'
   OR a.last LIKE 'i%'
   OR a.last LIKE 'o%'
   OR a.last LIKE 'u%'
GROUP BY a.last, b.title;