-- 15-list_score_counts.sql
-- Script to list the number of records with the same score.

-- Parameter: Database name
USE `dbname`;

-- List the number of records for each score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC, score DESC;
