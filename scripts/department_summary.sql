-- ---------------------------------------------------------------------------
-- Example queries for summarising the cleaned HR data
--
-- These statements assume you have loaded ``employee_talent_features.csv`` into a
-- database table named ``employee_talent_features``.  They demonstrate how to
-- compute the same metrics used in the Power BI dashboard using plain SQL.
-- Adjust the table and column names to match your database schema.

-- 1. Headcount by department
SELECT
    Department,
    COUNT(DISTINCT EmployeeNumber) AS employee_count
FROM employee_talent_features
GROUP BY Department
ORDER BY employee_count DESC;

-- 2. Average talent score and burnout risk by department
SELECT
    Department,
    AVG(Talent_Score)    AS avg_talent_score,
    AVG(Burnout_Risk)    AS avg_burnout_risk,
    AVG(Promotion_Readiness) AS avg_promotion_readiness
FROM employee_talent_features
GROUP BY Department
ORDER BY avg_talent_score DESC;

-- 3. Top 10 positions by promotion readiness
SELECT
    Position,
    AVG(Promotion_Readiness) AS avg_promotion_readiness
FROM employee_talent_features
GROUP BY Position
ORDER BY avg_promotion_readiness DESC
LIMIT 10;

-- 4. Employee satisfaction distribution
SELECT
    EmpSatisfaction,
    COUNT(*) AS employee_count
FROM employee_talent_features
GROUP BY EmpSatisfaction
ORDER BY EmpSatisfaction;

-- 5. Talent vs compensation correlation at the department level
SELECT
    Department,
    AVG(Salary)      AS avg_salary,
    AVG(Talent_Score) AS avg_talent_score
FROM employee_talent_features
GROUP BY Department
ORDER BY avg_salary DESC;
