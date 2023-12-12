-- 8-count_records_with_id.sql
-- Script to display the number of records with id

-- Parameter: Database name
USE `dbname`;

-- Display the number of records with id = 89
SELECT COUNT(*) AS count_records_with_id
FROM first_table
WHERE id = 89;
