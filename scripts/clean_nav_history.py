import pandas as pd
from pathlib import Path
df = pd.read_csv("data/raw/02_nav_history.csv")
print("Original Shape:", df.shape)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(["amfi_code", "date"])
df = df.drop_duplicates()
df = df[df["nav"] > 0]
df["nav"] = df.groupby("amfi_code")["nav"].ffill()
output_path = Path("data/processed")
output_path.mkdir(parents=True, exist_ok=True)
df.to_csv(
    output_path / "nav_history_clean.csv",
    index=False
)
print("Cleaned Shape:", df.shape)
print("Saved Successfully!")