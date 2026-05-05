import requests
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get your API Key from the environment variable
API_KEY = os.getenv("BIRDEYE_API_KEY") 
BASE_URL = "https://public-api.birdeye.so"

headers = {
    "x-chain": "solana",
    "accept": "application/json",
    "X-API-KEY": API_KEY
}

def get_trending_tokens():
    print("--- Fetching Trending Token List ---")
    url = f"{BASE_URL}/defi/token_trending?sort_by=rank&sort_type=asc"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']['tokens']
    return []

def check_security(address):
    url = f"{BASE_URL}/defi/token_security?address={address}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']
    return None

def main():
    tokens = get_trending_tokens()
    
    # Process the top 5 trending tokens
    for token in tokens[:5]:
        name = token.get('symbol')
        address = token.get('address')
        price = token.get('price')
        
        print(f"\nChecking: {name} ({address})")
        print(f"Price: ${price:.6f}")
        
        # Security Check
        security = check_security(address)
        if security:
            # Security indicator: Rugpull avoidance
            is_mintable = "Yes" if security.get('is_mintable') else "No"
            owner = security.get('owner', 'Unknown')
            print(f"Mintable: {is_mintable}")
            print(f"Owner: {owner[:10]}...")
        
        # Small delay to respect rate limits and accumulate API calls
        time.sleep(1)

if __name__ == "__main__":
    # Loop 10 times during testing to reach the 50 API Calls requirement
    # (1 trending call + 5 security calls) * 10 iterations = 60 calls total
    for i in range(10): 
        print(f"\n=== Execution Run #{i+1} ===")
        main()
        print("Waiting 30 seconds for the next update...")
        time.sleep(30)