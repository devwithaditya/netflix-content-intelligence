# Netflix Content Intelligence

## Live Dashboard
Deploy `index.html` and project files to Netlify for a live interactive dashboard.

## Project Overview
This is a complete Data Analytics portfolio project demonstrating the full analytics lifecycle:

**Raw Data → Data Cleaning → Feature Engineering → EDA → SQL Analysis → Interactive Dashboard**

## Dataset
Included demo dataset:
- 240 original content records
- 1 intentional duplicate for duplicate-removal testing
- 220 unique people available across cast/director generation
- 12 countries
- Multiple genres and ratings
- Movies and TV Shows
- Missing values for real cleaning demonstrations

## Run Everything Locally

### Option 1: Run analytics pipeline
Double-click:
`RUN_ANALYTICS_PIPELINE.bat`

This runs:
1. `01_data_cleaning.py`
2. `02_feature_engineering.py`
3. `03_eda.py`

Generated files:
- `data/processed/netflix_cleaned.csv`
- `data/processed/netflix_analytics.csv`
- `reports/data_quality_report.json`
- Charts inside `reports/figures/`

### Option 2: Run dashboard
Double-click:
`RUN_DASHBOARD.bat`

Open:
`http://localhost:8000`

## Python Analytics

### Data Cleaning
- Duplicate removal
- Missing value analysis
- String standardization
- Date conversion
- Data quality reporting

### Feature Engineering
- Year added
- Month added
- Duration value and unit
- Maturity category
- Content age
- Movie/TV flags

### Exploratory Data Analysis
- Content growth
- Top genres
- Top countries
- Rating distribution

## SQL
`sql/schema.sql` contains a normalized analytics schema.

`sql/analysis_queries.sql` contains 15 professional analytical SQL queries.

## Dashboard
Features:
- Interactive filters
- KPI cards
- Content growth
- Country analysis
- Genre analysis
- Content type analysis
- Dynamic business insights
- Dataset explorer

## Skills Demonstrated
Python • Pandas • Data Cleaning • Feature Engineering • EDA • SQL • Data Modeling • Data Visualization • HTML • CSS • JavaScript • Netlify Deployment

## Resume Description
Built an end-to-end Netflix Content Intelligence analytics platform using Python, Pandas, SQL and an interactive web dashboard. Performed data cleaning, duplicate detection, missing value analysis, feature engineering and exploratory data analysis; designed a normalized SQL schema with 15 analytical queries and deployed an interactive dashboard for real-time filtering and KPI analysis.
