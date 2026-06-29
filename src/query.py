import duckdb

DB_PATH = "data/onepiece.duckdb"

def run_analytics():
    conn = duckdb.connect(DB_PATH)
    
    print("\n📊 ONE PIECE EPISODE ANALYTICS")
    print("=" * 50)

    # 1. Total episodes breakdown
    print("\n1️⃣  Episode Breakdown")
    result = conn.execute("""
        SELECT
            COUNT(*) as total,
            SUM(CASE WHEN is_canon THEN 1 ELSE 0 END) as canon,
            SUM(CASE WHEN filler THEN 1 ELSE 0 END) as filler,
            SUM(CASE WHEN recap THEN 1 ELSE 0 END) as recap
        FROM episodes
    """).df()
    print(result.to_string(index=False))

    # 2. Top 10 highest rated episodes
    print("\n2️⃣  Top 10 Highest Rated Episodes")
    result = conn.execute("""
        SELECT episode_id, title, score
        FROM episodes
        WHERE score IS NOT NULL
        ORDER BY score DESC
        LIMIT 10
    """).df()
    print(result.to_string(index=False))

    # 3. Episodes per year
    print("\n3️⃣  Episodes Per Year")
    result = conn.execute("""
        SELECT year, COUNT(*) as episodes
        FROM episodes
        WHERE year IS NOT NULL
        GROUP BY year
        ORDER BY year
    """).df()
    print(result.to_string(index=False))

    # 4. Average score by year
    print("\n4️⃣  Average Score By Year")
    result = conn.execute("""
        SELECT year, ROUND(AVG(score), 2) as avg_score
        FROM episodes
        WHERE score IS NOT NULL AND year IS NOT NULL
        GROUP BY year
        ORDER BY year
    """).df()
    print(result.to_string(index=False))

    # 5. Filler percentage
    print("\n5️⃣  Filler Percentage")
    result = conn.execute("""
        SELECT
            ROUND(100.0 * SUM(CASE WHEN filler THEN 1 ELSE 0 END) / COUNT(*), 2) as filler_pct,
            ROUND(100.0 * SUM(CASE WHEN is_canon THEN 1 ELSE 0 END) / COUNT(*), 2) as canon_pct
        FROM episodes
    """).df()
    print(result.to_string(index=False))

    conn.close()


if __name__ == "__main__":
    run_analytics()