# 🏴‍☠️ One Piece ETL Pipeline

A data engineering pipeline that extracts, transforms, and analyzes all 1164 One Piece episodes using Python, Pandas, and DuckDB.

## 🔧 Tech Stack
- **Python 3.12** — core language
- **Requests** — REST API ingestion (Jikan API)
- **Pandas** — data transformation
- **DuckDB** — local analytical database
- **Jikan API** — free MyAnimeList data source

## 📊 Pipeline Architecture

Jikan API → Extract → Transform → Load (DuckDB) → SQL Analytics

## 🔍 Key Insights
- 1164 total episodes fetched
- 91% canon, 8.3% filler
- Highest rated: Episode 396 (score: 4.88)
- Scores trending upward since 2010

## 🚀 How to Run
```bash
git clone git@github.com:Subbu-vasanth/anime-etl.git
cd anime-etl
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## 📁 Project Structure

anime-etl/

├── src/

│   ├── extract.py    # API ingestion

│   ├── transform.py  # Pandas cleaning

│   ├── load.py       # DuckDB loader

│   └── query.py      # SQL analytics

├── main.py           # Pipeline entry point

└── requirements.txt