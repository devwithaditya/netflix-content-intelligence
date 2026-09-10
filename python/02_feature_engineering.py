from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data/processed/netflix_cleaned.csv"
OUTPUT = ROOT / "data/processed/netflix_analytics.csv"

MATURITY = {
    "TV-Y":"Kids", "TV-Y7":"Kids", "TV-G":"Kids", "G":"Kids",
    "TV-PG":"Teen", "PG":"Teen", "PG-13":"Teen", "TV-14":"Teen",
    "TV-MA":"Adult", "R":"Adult", "NC-17":"Adult"
}

def main():
    df = pd.read_csv(INPUT)
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
    df["year_added"] = df["date_added"].dt.year
    df["month_added"] = df["date_added"].dt.month
    df["month_name"] = df["date_added"].dt.month_name()

    duration = df["duration"].str.extract(r"(?P<duration_value>\d+)\s*(?P<duration_unit>.*)")
    df["duration_value"] = pd.to_numeric(duration["duration_value"], errors="coerce")
    df["duration_unit"] = duration["duration_unit"].str.strip()

    df["maturity_category"] = df["rating"].map(MATURITY).fillna("Unknown")
    df["content_age"] = pd.Timestamp.now().year - df["release_year"]
    df["is_movie"] = (df["type"] == "Movie").astype(int)
    df["is_tv_show"] = (df["type"] == "TV Show").astype(int)

    df.to_csv(OUTPUT, index=False)
    print(f"Feature engineering completed. Saved {len(df)} records to {OUTPUT}")

if __name__ == "__main__":
    main()
