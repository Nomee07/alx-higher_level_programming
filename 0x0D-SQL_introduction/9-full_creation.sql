-- 9-create_second_table_and_insert_rows.sql
-- Script to create the table.

-- Parameter: Database name
USE `dbname`;

-- Create the table second_table if it doesn't exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insert multiple rows into the table second_table
INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
