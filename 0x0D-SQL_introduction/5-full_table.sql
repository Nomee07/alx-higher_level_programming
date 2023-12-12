-- 5-print_table_description.sql
-- Script to print the full description of the table

-- Parameter: Database name
USE `dbname`;

-- Get the table columns information
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'first_table' AND TABLE_SCHEMA = 'dbname';
