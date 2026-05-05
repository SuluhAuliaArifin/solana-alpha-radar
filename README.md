# 🚀 Solana Alpha Radar (Birdeye BIP Sprint 3)

[English](#english) | [Bahasa Indonesia](#bahasa-indonesia)

---

# English

## 📝 Description

**Solana Alpha Radar** is a lightweight terminal-based monitoring tool built for the Solana ecosystem. It identifies high-momentum tokens by integrating Birdeye’s trending data with real-time pricing and security insights.

This project was developed as part of the Birdeye Data 4-Week BIP Competition (Sprint 3).

---

## 💡 Why This Matters

In fast-moving on-chain markets like Solana, traders often miss early opportunities due to lack of real-time insights.

Solana Alpha Radar bridges this gap by combining:

* Trending momentum signals
* Real-time price tracking
* Basic security analysis

This enables faster and more informed decision-making.

---

## ✨ Features

* 🔥 Top 5 Trending Tracker — Automatically fetches trending tokens
* 💰 Real-Time Price — Displays latest market price
* 🛡️ Security Check — Detects mintable tokens & ownership
* ⚠️ Risk Indicator — Warns about potential risky tokens

---

## 🛠️ Tech Stack

* Python
* Birdeye API
* Requests
* Python-dotenv

---

## 📊 Birdeye Endpoints Used

* `/defi/token_trending` → Identify trending tokens
* `/defi/price` → Retrieve real-time prices
* `/defi/token_security` → Analyze token risks

---

## 📸 Example Output

![Terminal Output](./Screenshot.png)

---

## 🧪 Sample Output

```
Memeriksa: swarms (...)
Harga: $0.031650
Mintable: Tidak
Owner: 7gHk9sK2...
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/SuluhAuliaArifin/solana-alpha-radar.git
cd solana-alpha-radar
```

---

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate:

* Windows:

```bash
venv\Scripts\activate
```

* Linux / Mac:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Jika belum ada `requirements.txt`, install manual:

```bash
pip install requests python-dotenv
```

---

### 4. Setup Environment Variables

Buat file `.env` di root project:

📄 `.env`

```
BIRDEYE_API_KEY=your_api_key_here
```

---

### 5. Run the Application

```bash
python main.py
```

---

## 🔐 Notes

* Pastikan API Key dari Birdeye aktif
* Jangan commit file `.env` ke repository
* Gunakan `.gitignore` untuk keamanan

---

## 📂 Project Structure (Recommended)

```
solana-alpha-radar/
│── main.py
│── services/
│   ├── birdeye_api.py
│── utils/
│   ├── formatter.py
│── .env
│── requirements.txt
│── README.md
```

---

## 🚀 Future Improvements

* Web dashboard (Flask / FastAPI)
* Telegram / Discord bot integration
* Historical tracking & analytics
* Alert system for high-risk tokens

---

# Bahasa Indonesia

## 📝 Deskripsi

**Solana Alpha Radar** adalah alat monitoring berbasis terminal yang ringan untuk ekosistem Solana. Tool ini mengidentifikasi token dengan momentum tinggi dengan menggabungkan data trending dari Birdeye, harga real-time, dan analisis keamanan.

Project ini dibuat sebagai bagian dari kompetisi **Birdeye Data 4-Week BIP (Sprint 3)**.

---

## 💡 Kenapa Ini Penting

Di pasar on-chain seperti Solana yang bergerak cepat, banyak trader kehilangan peluang karena kurangnya data real-time.

Solana Alpha Radar membantu dengan menggabungkan:

* Data token trending
* Harga real-time
* Analisis keamanan dasar

Sehingga keputusan trading bisa lebih cepat dan tepat.

---

## ✨ Fitur

* 🔥 Tracker Top 5 Trending
* 💰 Harga Real-Time
* 🛡️ Cek Keamanan Token
* ⚠️ Indikator Risiko

---

## ⚙️ Cara Install & Jalankan

### 1. Clone Repo

```bash
git clone https://github.com/SuluhAuliaArifin/solana-alpha-radar.git
cd solana-alpha-radar
```

### 2. Install Dependency

```bash
pip install -r requirements.txt
```

### 3. Setup API Key

Buat file `.env`:

```
BIRDEYE_API_KEY=your_api_key_here
```

### 4. Jalankan

```bash
python main.py
```

---

## 🔐 Catatan

* Jangan upload `.env` ke GitHub
* Gunakan `.gitignore`
* Pastikan API aktif

---

## 🤝 Contributing

Pull request sangat terbuka. Silakan fork dan kembangkan 🚀

---

## 📜 License

MIT License
