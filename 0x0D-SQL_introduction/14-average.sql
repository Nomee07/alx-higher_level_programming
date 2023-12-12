-- 14-compute_score_average.sql
-- Script to compute the score average of all records.

-- Compute the average score of all records
ELECT AVG(`score`) AS `average`
FROM `second_table`;
