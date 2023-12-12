-- 4-create_table_if_not_exists.sql
-- Script to create the table first_table if it doesn't exist in the specified database.

-- Parameter: Database name
USE `dbname`;

-- Create the table only if it doesn't exist
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
