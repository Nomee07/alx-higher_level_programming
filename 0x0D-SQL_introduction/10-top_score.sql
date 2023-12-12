-- 10-list_records_second_table.sql
-- Script to list all records of the table.

-- Parameter: Database name
USE `dbname`;

-- List all records of the table second_table, ordered by score (top first)
SELECT score, name
FROM second_table
ORDER BY score DESC;
