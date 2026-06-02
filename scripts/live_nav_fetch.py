import requests
import pandas as pd
from pathlib import Path

schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

output_folder = Path("data/raw")
output_folder.mkdir(parents=True, exist_ok=True)

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data["data"])

    filename = output_folder / f"{name}.csv"

    df.to_csv(filename, index=False)

    print(f"Saved: {filename}")
    print(f"Rows: {len(df)}")
    print("-" * 40)