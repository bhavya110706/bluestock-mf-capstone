from pathlib import Path
import pandas as pd

data_folder = Path("data/raw")

csv_files = list(data_folder.glob("*.csv"))

print("=" * 60)
print(f"Found {len(csv_files)} CSV files")
print("=" * 60)

for file in csv_files:

    print(f"\nProcessing: {file.name}")

    try:
        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        df["date"] = pd.to_datetime(df["date"], dayfirst=True)
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\n" + "=" * 60)

    except Exception as e:
        print(f"Error reading {file.name}: {e}")