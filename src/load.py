import duckdb
import pandas as pd

DB_PATH = "data/onepiece.duckdb"

def load_episodes(df: pd.DataFrame):
    print("Loading into DuckDB...")
    
    conn = duckdb.connect(DB_PATH)
    
    # Drop table if exists (fresh load every run)
    conn.execute("DROP TABLE IF EXISTS episodes")
    
    # Create table from dataframe directly
    conn.execute("""
        CREATE TABLE episodes AS
        SELECT * FROM df
    """)
    
    # Verify
    count = conn.execute("SELECT COUNT(*) FROM episodes").fetchone()[0]
    print(f"Loaded {count} episodes into DuckDB at {DB_PATH}")
    
    conn.close()
    return count


if __name__ == "__main__":
    from extract import get_one_piece_episodes
    from transform import transform_episodes
    raw = get_one_piece_episodes()
    df = transform_episodes(raw)
    load_episodes(df)