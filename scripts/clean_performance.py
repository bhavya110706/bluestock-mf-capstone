import pandas as pd
from pathlib import Path
df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)
print("Original Shape:", df.shape)
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]
for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )
df = df[
    (df["expense_ratio_pct"] >= 0.1)
    &
    (df["expense_ratio_pct"] <= 2.5)
]
df = df.drop_duplicates()
Path("data/processed").mkdir(
    parents=True,
    exist_ok=True
)
df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)
print("Cleaned Shape:", df.shape)
print("Saved Successfully!")