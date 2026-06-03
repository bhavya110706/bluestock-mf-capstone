-- Top 5 funds by AUM
SELECT * FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- Transaction count by state
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state;

-- Expense ratio < 1%
SELECT *
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Top 5 returns
SELECT *
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- Highest Sharpe Ratio
SELECT *
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- Risk grade distribution
SELECT risk_grade, COUNT(*)
FROM dim_fund
GROUP BY risk_grade;

-- Transaction type count
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- Average AUM
SELECT AVG(aum_crore)
FROM fact_aum;

-- Highest NAV
SELECT MAX(nav)
FROM fact_nav;