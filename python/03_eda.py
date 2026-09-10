from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/processed/netflix_analytics.csv"
FIG = ROOT / "reports/figures"
FIG.mkdir(parents=True, exist_ok=True)

def save_bar(series, title, xlabel, filename):
    plt.figure(figsize=(10,5))
    series.sort_values().plot(kind="barh")
    plt.title(title); plt.xlabel(xlabel); plt.tight_layout()
    plt.savefig(FIG/filename, dpi=150); plt.close()

def main():
    df = pd.read_csv(DATA)

    # Content growth
    growth = df.dropna(subset=["year_added"]).groupby("year_added").size()
    plt.figure(figsize=(10,5))
    growth.plot(kind="line", marker="o")
    plt.title("Netflix Content Added Over Time")
    plt.xlabel("Year Added"); plt.ylabel("Titles")
    plt.tight_layout(); plt.savefig(FIG/"content_growth.png", dpi=150); plt.close()

    # Top genres
    genre_df = df.assign(genre=df["listed_in"].str.split(",")).explode("genre")
    genre_df["genre"] = genre_df["genre"].str.strip()
    save_bar(genre_df["genre"].value_counts().head(10), "Top 10 Genres", "Titles", "top_genres.png")

    # Top countries
    country_df = df.assign(country_name=df["country"].str.split(",")).explode("country_name")
    country_df["country_name"] = country_df["country_name"].str.strip()
    save_bar(country_df["country_name"].value_counts().head(10), "Top 10 Countries", "Titles", "top_countries.png")

    # Rating distribution
    save_bar(df["rating"].value_counts(), "Rating Distribution", "Titles", "ratings.png")

    print("EDA completed. Figures saved in reports/figures")

if __name__ == "__main__":
    main()
