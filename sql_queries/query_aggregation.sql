SELECT
    CASE WHEN SUM(year_published) / AVG(year_published) = COUNT(DISTINCT year_published)
        THEN 'All publication years are distinct.'
        ELSE 'Not all publication years are distinct.'
    END
FROM books;