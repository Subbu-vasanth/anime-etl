import pandas as pd

def transform_episodes(raw_episodes):
    print("Transforming episodes...")
    
    df = pd.DataFrame(raw_episodes)
    
    # Keep only useful columns
    df = df[[
        "mal_id",
        "title",
        "title_romanji",
        "aired",
        "score",
        "filler",
        "recap"
    ]]
    
    # Rename for clarity
    df.rename(columns={
        "mal_id": "episode_id",
        "title_romanji": "title_romanji",
        "aired": "air_date",
    }, inplace=True)
    
    # Clean types
    df["air_date"] = pd.to_datetime(df["air_date"], errors="coerce")
    df["score"] = pd.to_numeric(df["score"], errors="coerce")
    df["filler"] = df["filler"].astype(bool)
    df["recap"] = df["recap"].astype(bool)
    
    # Add derived columns
    df["year"] = df["air_date"].dt.year
    df["month"] = df["air_date"].dt.month
    df["is_canon"] = ~df["filler"] & ~df["recap"]
    
    print(f"Transformed {len(df)} episodes")
    print(f"Columns: {list(df.columns)}")
    
    return df


if __name__ == "__main__":
    from extract import get_one_piece_episodes
    raw = get_one_piece_episodes()
    df = transform_episodes(raw)
    print(df.head())