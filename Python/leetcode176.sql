-- Second Highest Salary

-- tricky to handle 'null'

-- Write your MySQL query statement below
SELECT max(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT max(Salary) FROM Employee)


-- WRONG
WHERE Salary < (SELECT MAX(SALARY) FROM Employee)
ORDER BY Salary DESC
LIMIT 1
