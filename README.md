# 🚀 Solana Alpha Radar (Birdeye BIP Sprint 3)

[English](#english) | [Bahasa Indonesia](#bahasa-indonesia)

---

# English

## 📝 Description

**Solana Alpha Radar** is a lightweight terminal-based on-chain intelligence tool built for the Solana ecosystem. It identifies high-momentum tokens by integrating Birdeye’s trending data with real-time pricing and basic security insights.

This project was developed as part of the **Birdeye Data 4-Week BIP Competition (Sprint 3)**.

The system is designed as a **minimal alpha detection engine** that helps surface potential market opportunities earlier through structured data analysis.

---

## 💡 Why This Matters

In fast-moving on-chain ecosystems like Solana, opportunities appear and disappear quickly. Most traders lack a structured way to interpret raw token data.

Solana Alpha Radar solves this by:

- Aggregating trending token signals
- Monitoring real-time price movement
- Checking basic security risks
- Providing fast interpretative output (alpha signals)

This enables faster and more informed decision-making in volatile markets.

---

## ✨ Features

- 🔥 Top 5 Trending Tracker — Fetches and monitors trending Solana tokens  
- 💰 Real-Time Price Feed — Displays live token pricing data  
- 🛡️ Security Analysis — Detects mint authority risks and ownership signals  
- ⚠️ Risk Indicator System — Simple classification of token safety level  
- 🧠 Basic Alpha Insight Layer — Converts raw data into readable signals  

---

## 🧠 System Workflow

1. Fetch trending tokens from Birdeye API  
2. Retrieve token price and metadata  
3. Perform security validation  
4. Apply scoring logic (custom heuristic model)  
5. Generate insight classification  
6. Output structured alpha report in terminal  

---

## 🛠️ Tech Stack

- Python 3.x  
- Requests (HTTP client)  
- python-dotenv (environment configuration)  
- Birdeye API (Solana data provider)  

---

## 📊 Birdeye Endpoints Used

- `/defi/token_trending` → Fetch trending tokens  
- `/defi/token_security` → Security and mint analysis  
- `/defi/token_overview` → Token metadata enrichment  

---

## 📸 Example Output

```text
Checking: ZEREBRO

Price: $0.034120

🔥 ALPHA REPORT
Token   : ZEREBRO
Score   : 75 (🔥 HIGH MOMENTUM)
Insight : Breakout Potential
Security: Low Risk


⚙️ Installation & Setup
1. Clone Repository
git clone https://github.com/SuluhAuliaArifin/solana-alpha-radar.git
cd solana-alpha-radar
2. Create Virtual Environment (Recommended)
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt

If not available:

pip install requests python-dotenv
4. Setup Environment Variables

Create .env file:

BIRDEYE_API_KEY=your_api_key_here
5. Run Application
python main.py
🔐 Security Notes
Never commit .env to GitHub
Use .gitignore for sensitive files
Keep API keys private
Respect API rate limits
📂 Project Structure
solana-alpha-radar/
│
├── main.py
├── app/
│   ├── services/
│   │   ├── scoring_service.py
│   │   ├── insight_service.py
│   └── utils/
│       ├── formatter.py
│
├── .env
├── requirements.txt
├── README.md
🚀 Future Improvements
Web dashboard (Flask / FastAPI)
Real-time WebSocket streaming
Wallet flow tracking (whale detection)
Machine learning-based scoring model
Alert system for breakout tokens
Historical backtesting engine
⚠️ Limitations
Dependent on external API availability
Rule-based scoring (not AI/ML yet)
Limited historical context
Basic heuristic insights
📌 Project Philosophy

"Turning raw on-chain data into actionable alpha signals with minimal complexity."

👤 Author

Built as part of exploration into Solana ecosystem analytics and alpha detection systems.

📜 License

MIT License

Bahasa Indonesia
📝 Deskripsi

Solana Alpha Radar adalah alat monitoring berbasis terminal untuk ekosistem Solana. Tool ini mendeteksi token dengan momentum tinggi menggunakan data trending dari Birdeye, harga real-time, dan analisis keamanan dasar.

Project ini dibuat sebagai bagian dari kompetisi Birdeye Data 4-Week BIP (Sprint 3).

💡 Tujuan

Di ekosistem on-chain yang bergerak cepat, banyak peluang terlewat karena kurangnya sistem analisis data yang terstruktur.

Solana Alpha Radar membantu dengan:

Menggabungkan data token trending
Analisis harga real-time
Cek risiko keamanan
Output insight sederhana
✨ Fitur
🔥 Tracker Token Trending
💰 Harga Real-Time
🛡️ Analisis Keamanan Token
⚠️ Indikator Risiko
🧠 Insight Alpha Sederhana
⚙️ Cara Menjalankan
git clone https://github.com/SuluhAuliaArifin/solana-alpha-radar.git
cd solana-alpha-radar
pip install -r requirements.txt
python main.py
🔐 Catatan Penting
Jangan upload .env
Gunakan .gitignore
Pastikan API key aktif
📜 License

MIT License
