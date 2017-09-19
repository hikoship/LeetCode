-- Shortest Distance in a Line

-- join

-- Table point holds the x coordinate of some points on x-axis in a plane, which are all integers.
--
-- Write a query to find the shortest distance between two points in these points.
-- | x   |
-- |-----|
-- | -1  |
-- | 0   |
-- | 2   |
-- The shortest distance is '1' obviously, which is from point '-1' to '0'. So the output is as below:
-- | shortest|
-- |---------|
-- | 1       |
-- Note: Every point is unique, which means there is no duplicates in table point.
-- Follow-up: What if all these points have an id and are arranged from the left most to the right most of x axis?

-- Write your MySQL query statement below
SELECT MIN(t1.x - t2.x) AS shortest
FROM point AS t1, point AS t2
WHERE t1.x > t2.x

SELECT MIN(t1.x - t2.x) AS shortest
FROM point AS t1 JOIN point AS t2
ON t1.x > t2.x
