import pandas as pd

# Load performance data
performance = pd.read_csv(
    "../data/processed/scheme_performance_clean.csv"
)

risk = input(
    "Enter Risk Appetite (Low / Moderate / High): "
)

# Map user input
if risk == "Low":
    selected = ["Low"]

elif risk == "Moderate":
    selected = [
        "Moderate",
        "Moderately High"
    ]

elif risk == "High":
    selected = [
        "High",
        "Very High"
    ]

else:
    print("Invalid Risk Level")
    exit()

recommendations = (
    performance[
        performance["risk_grade"]
        .isin(selected)
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print("\nTop 3 Recommended Funds:\n")

print(
    recommendations[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ]
)