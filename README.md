# 🚀 Crypto Arbitrage Scanner & Real-Time Discrepancy Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg?logo=python)](https://www.python.org/)
[![Actions: Cloud Cron](https://img.shields.io/badge/GitHub%20Actions-Cloud%20Cron%20Active-brightgreen.svg?logo=githubactions)](https://github.com/whyst0ne/crypto-arbitrage-scanner/actions)
[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa?style=flat&logo=github)](https://github.com/sponsors/whyst0ne)

A high-performance, automated multi-exchange cryptocurrency arbitrage detector built with Python and CCXT. Monitors order books across top Tier-1 exchanges (Kraken, Bybit, KuCoin, Gate.io, Bitget) in real time to spot triangular and cross-exchange spatial price discrepancies.

---

## ⚡ Features
- **Zero API Keys Required:** Queries public real-time ticker and orderbook data without account restrictions.
- **5+ Tier-1 Exchanges Supported:** Kraken, Bybit, KuCoin, Gate.io, and Bitget.
- **Top Liquid Pairs Monitored:** `BTC/USDT`, `ETH/USDT`, `SOL/USDT`, `XRP/USDT`, `DOGE/USDT`.
- **Fee-Adjusted Net Calculations:** Automatically subtracts taker and withdrawal fees to guarantee real net profit signals.
- **Webhook & Signal Logging:** Exports actionable alerts to `arbitrage_signals.json` or webhook triggers.
- **Autonomous Cloud Cron:** Runs continuously every 30 minutes via GitHub Actions workflows with zero server costs.

---

## 🛠️ Quickstart

```bash
git clone https://github.com/whyst0ne/crypto-arbitrage-scanner.git
cd crypto-arbitrage-scanner
pip install -r requirements.txt
python scanner.py
```

---

## 📊 Sample Output
```text
Pair: BTC/USDT   | Buy: bitget   @ 84378.59 | Sell: kraken   @ 84399.50 | Gross: +0.025%
Pair: ETH/USDT   | Buy: bitget   @ 2503.51  | Sell: kraken   @ 2504.30  | Gross: +0.032%
Pair: SOL/USDT   | Buy: bybit    @ 107.96   | Sell: kraken   @ 107.98   | Gross: +0.019%
```

---

## 💎 Donations & Sponsorships
If this tool generates profit for your trading desk, consider supporting ongoing development:

- **EVM (Base / Arbitrum / Ethereum / Polygon / Gnosis):** `0xe5ab26877172254b72f3ae6da5789d2468b7b282`
- **USDC / USDT / DAI:** Supported on Base, Polygon, and Arbitrum

---
*Disclaimer: Not financial advice. Always verify gas, deposit latency, and exchange withdrawal limits before executing automated orders.*
