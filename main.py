import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

# Ganti dengan API Key baru kamu
API_KEY = os.getenv("BIRDEYE_API_KEY") 
BASE_URL = "https://public-api.birdeye.so"

headers = {
    "x-chain": "solana",
    "accept": "application/json",
    "X-API-KEY": API_KEY
}

def get_trending_tokens():
    print("--- Mengambil Daftar Token Trending ---")
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
    
    # Ambil 5 token teratas untuk dicek
    for token in tokens[:5]:
        name = token.get('symbol')
        address = token.get('address')
        price = token.get('price')
        
        print(f"\nMemeriksa: {name} ({address})")
        print(f"Harga: ${price:.6f}")
        
        # Cek Keamanan
        security = check_security(address)
        if security:
            # Contoh indikator keamanan: rugpull avoidance
            is_mintable = "Ya" if security.get('is_mintable') else "Tidak"
            owner = security.get('owner', 'Unknown')
            print(f"Mintable: {is_mintable}")
            print(f"Owner: {owner[:10]}...")
        
        # Delay kecil agar tidak terkena rate limit dan pelan-pelan hit API calls
        time.sleep(1)

if __name__ == "__main__":
    # Jalankan loop ini beberapa kali saat kamu testing 
    # untuk mencapai syarat 50 API Calls
    for i in range(10): 
        print(f"\n=== Running ke-{i+1} ===")
        main()
        print("Menunggu 30 detik untuk update berikutnya...")
        time.sleep(30)