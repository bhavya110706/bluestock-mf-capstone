import pandas as pd
from pathlib import Path
df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)
print("Original Shape:", df.shape)
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)
valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]
df = df[
    df["transaction_type"].isin(valid_types)
]
df = df[df["amount_inr"] > 0]
valid_kyc = [
    "Verified",
    "Pending"
]
df = df[
    df["kyc_status"].isin(valid_kyc)
]
df = df.drop_duplicates()
Path("data/processed").mkdir(
    parents=True,
    exist_ok=True
)
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)
print("Cleaned Shape:", df.shape)
print("Saved Successfully!")