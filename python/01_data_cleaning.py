from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data/raw/netflix_titles.csv"
OUTPUT = ROOT / "data/processed/netflix_cleaned.csv"
REPORT = ROOT / "reports/data_quality_report.json"

def main():
    df = pd.read_csv(INPUT)
    initial_rows = len(df)
    missing_before = df.isna().sum().to_dict()

    duplicates = int(df.duplicated().sum())
    df = df.drop_duplicates().copy()

    # Standardize strings
    for col in ["type","title","director","cast","country","rating","duration","listed_in","description"]:
        df[col] = df[col].fillna("").astype(str).str.strip()

    # Parse date safely
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

    # Preserve missing-data information before replacing analytical values
    df["has_director"] = (df["director"] != "").astype(int)
    df["has_cast"] = (df["cast"] != "").astype(int)
    df["has_country"] = (df["country"] != "").astype(int)
    df["has_rating"] = (df["rating"] != "").astype(int)

    # Replace missing dimensions with Unknown
    for col in ["director","cast","country","rating","listed_in"]:
        df[col] = df[col].replace("", "Unknown")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)

    report = {
        "initial_rows": initial_rows,
        "rows_after_duplicate_removal": len(df),
        "duplicates_removed": duplicates,
        "missing_values_before_cleaning": missing_before,
        "missing_values_after_cleaning": df.isna().sum().to_dict(),
        "columns": list(df.columns)
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2, default=str))
    print("Data cleaning completed successfully")
    print(json.dumps(report, indent=2, default=str))

if __name__ == "__main__":
    main()
