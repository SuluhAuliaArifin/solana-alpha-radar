import sys
import os
import requests
import time
from dotenv import load_dotenv

# Menambahkan path agar folder lokal terbaca
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.services.scoring_service import calculate_score
from app.services.insight_service import generate_insight
from app.utils.formatter import classify_score, print_token_report

# Load environment variables
load_dotenv()

# Konfigurasi API Birdeye
API_KEY = os.getenv("BIRDEYE_API_KEY") 
BASE_URL = "https://public-api.birdeye.so"

headers = {
    "x-chain": "solana",
    "accept": "application/json",
    "X-API-KEY": API_KEY or ""
}

def safe_get(url):
    """Fungsi helper untuk request ke API dengan penanganan error"""
    try:
        if not API_KEY:
            print("[ERROR] API Key tidak ditemukan di file .env!")
            return None
            
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            print(f"[ERROR] API Key tidak valid (401).")
        elif response.status_code == 429:
            print(f"[ERROR] Rate limit tercapai. Menunggu sebentar...")
            time.sleep(5)
        else:
            print(f"[ERROR] Status {response.status_code} untuk {url}")
            
    except requests.exceptions.Timeout:
        print(f"[ERROR] Koneksi Timeout ke {url}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Terjadi masalah koneksi: {e}")
    except KeyboardInterrupt:
        raise # Biarkan KeyboardInterrupt ditangani di loop utama
    
    return None

def get_trending_tokens():
    print("\n--- Fetching Trending Token List ---")
    url = f"{BASE_URL}/defi/token_trending?sort_by=rank&sort_type=asc"
    
    data = safe_get(url)
    if data and data.get('success'):
        return data.get('data', {}).get('tokens', [])
    
    return []

def check_security(address):
    url = f"{BASE_URL}/defi/token_security?address={address}"
    data = safe_get(url)
    if data and data.get('success'):
        return data.get('data')
    return None

def get_token_overview(address):
    url = f"{BASE_URL}/defi/token_overview?address={address}"
    data = safe_get(url)
    if data and data.get('success'):
        return data.get('data', {})
    return {}

def main():
    tokens = get_trending_tokens()
    
    if not tokens:
        print("[!] Tidak ada data token trending yang ditemukan.")
        return

    # Process top 5 trending tokens
    for token in tokens[:5]:
        try:
            name = token.get('symbol', 'Unknown')
            address = token.get('address')
            price = token.get('price', 0)
            
            if not address:
                continue

            print(f"\nChecking: {name} ({address})")
            print(f"Price: ${price:.6f}")
            
            # Ambil data overview
            overview = get_token_overview(address)
            time.sleep(0.5) # Jeda singkat untuk kestabilan

            # Gabungkan data untuk scoring
            combined_data = {**token, **overview}

            # Hitung score dan insight
            score = calculate_score(combined_data)
            category = classify_score(score)
            insight = generate_insight(combined_data)
            
            # Cek keamanan
            security = check_security(address)
            time.sleep(0.5)

            # Print laporan (fungsi dari app.utils.formatter)
            print_token_report(
                name, address, price,
                score, category, insight,
                security
            )
            
            # Jeda antar token agar tidak terkena rate limit
            time.sleep(1)
            
        except Exception as e:
            print(f"[!] Gagal memproses token {token.get('symbol')}: {e}")
            continue

if __name__ == "__main__":
    try:
        # Loop 10 kali
        for i in range(10): 
            print(f"\n=== Execution Run #{i+1} ===")
            main()
            
            if i < 9: # Jangan print pesan tunggu di iterasi terakhir
                print(f"\nWaiting 30 seconds for the next update (Run #{i+2})...")
                time.sleep(30)
                
    except KeyboardInterrupt:
        print("\n\n[!] Program dihentikan oleh pengguna. Keluar...")
        sys.exit(0)
    except Exception as e:
        print(f"\n[CRITICAL ERROR] {e}")
        sys.exit(1)