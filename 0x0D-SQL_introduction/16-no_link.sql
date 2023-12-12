-- 16-list_records_with_names.sql
-- Script to list all records with a name value.

-- Parameter: Database name
USE `dbname`;

-- List all records with a name value, ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
