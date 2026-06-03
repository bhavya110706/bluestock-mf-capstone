# Data Dictionary

## 01_fund_master.csv
- amfi_code : Unique AMFI scheme code
- scheme_name : Mutual fund scheme name
- fund_house : AMC name
- category : Scheme category
- plan : Direct/Regular
- risk_grade : Risk classification

## 02_nav_history.csv
- amfi_code : Scheme code
- date : NAV date
- nav : Net Asset Value

## 08_investor_transactions.csv
- investor_id : Unique investor ID
- transaction_date : Transaction date
- transaction_type : SIP/Lumpsum/Redemption
- amount_inr : Transaction amount

## 07_scheme_performance.csv
- return_1yr_pct : 1 year return
- return_3yr_pct : 3 year return
- return_5yr_pct : 5 year return
- alpha : Alpha metric
- beta : Beta metric
- sharpe_ratio : Risk adjusted return
- expense_ratio_pct : Expense ratio

Source:
BlueStock Capstone Dataset