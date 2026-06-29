import requests
import time

BASE_URL = "https://api.jikan.moe/v4"

def get_one_piece_episodes():
    episodes = []
    page = 1
    
    print("Fetching One Piece episodes from Jikan API...")
    
    while True:
        url = f"{BASE_URL}/anime/21/episodes?page={page}"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Error on page {page}: {response.status_code}")
            break
        
        data = response.json()
        batch = data["data"]
        
        if not batch:
            break
        
        episodes.extend(batch)
        print(f"  Page {page} fetched — {len(batch)} episodes")
        
        if not data["pagination"]["has_next_page"]:
            break
        
        page += 1
        time.sleep(0.5)
    
    print(f"Total episodes fetched: {len(episodes)}")
    return episodes


if __name__ == "__main__":
    eps = get_one_piece_episodes()
    print(eps[0])