import sys
from src.extract import get_one_piece_episodes
from src.transform import transform_episodes
from src.load import load_episodes
from src.query import run_analytics

def main():
    print("🚀 Starting Anime ETL Pipeline...")
    try:
        # 1. Extract
        raw_data = get_one_piece_episodes()
        if not raw_data:
            print("❌ Extraction failed: No data retrieved.")
            sys.exit(1)
            
        # 2. Transform
        df = transform_episodes(raw_data)
        
        # 3. Load
        load_count = load_episodes(df)
        
        # 4. Query / Analyze
        run_analytics()
        
        print("\n🎉 ETL Pipeline execution finished successfully!")
        
    except Exception as e:
        print(f"\n❌ ETL Pipeline failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()