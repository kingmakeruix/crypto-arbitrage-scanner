# 🚀 Crypto Arbitrage Scanner, DeFi Flashloan Keeper & x402 Signal Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg?logo=python)](https://www.python.org/)
[![Actions: Cloud Cron](https://img.shields.io/badge/GitHub%20Actions-Cloud%20Cron%20Active-brightgreen.svg?logo=githubactions)](https://github.com/whyst0ne/crypto-arbitrage-scanner/actions)
[![x402 Payment Gateway](https://img.shields.io/badge/x402-USDC%20Micro--Payments-6f42c1.svg)](https://github.com/whyst0ne/crypto-arbitrage-scanner)
[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa?style=flat&logo=github)](https://github.com/sponsors/whyst0ne)

A high-performance, zero-API-key CEX & DEX cryptocurrency arbitrage detector and Aave V3 Flashloan calldata generator built with Python. Monitors real-time order books across top Tier-1 exchanges (**Binance, Kraken, Coinbase, Bybit, KuCoin**) and L2 DEX liquidity pools (**Base Aerodrome/Uniswap V3, Arbitrum Camelot/SushiSwap**).

---

## ⚡ Core Capabilities
- **Zero API Keys Required:** Queries public real-time orderbook ticker endpoints (`bookTicker`) and on-chain DEX slot0/reserves via public RPCs.
- **CEX Spatial Arbitrage Feed:** Live cross-exchange spread monitoring for `BTC/USDT`, `ETH/USDT`, `SOL/USDT`, and `XRP/USDT`, published automatically to [`arbitrage_signals.json`](./arbitrage_signals.json).
- **Zero-Capital Aave V3 Flashloan Keeper (`defi_keeper_bot.py`):** Generates standard 266-byte ABI-encoded `flashLoanSimple` calldata to capture on-chain DEX price discrepancies with $0 upfront capital.
- **x402 HTTP Micro-Payment Gateway (`x402_server.py`):** Implements the `HTTP 402 Payment Required` standard so autonomous AI agents can unlock live Flashloan execution payloads via on-chain Base USDC settlement.
- **Model Context Protocol (MCP) Server (`mcp_agent_server.py`):** JSON-RPC 2.0 stdio server exposing `get_live_flashloan_signals` and `get_payment_instructions` tools directly to Claude Desktop, Cursor, and autonomous agents.

---

## 📊 Latest Live Signal Snapshot (`arbitrage_signals.json`)
```json
[
  {
    "pair": "BTC/USDT",
    "buy_exchange": "Kraken",
    "buy_price": 81788.0,
    "sell_exchange": "Binance",
    "sell_price": 81792.13,
    "spread_usd": 4.13,
    "spread_pct": 0.005,
    "timestamp": "2026-10-23 17:21:03 UTC"
  },
  {
    "pair": "ETH/USDT",
    "buy_exchange": "Binance",
    "buy_price": 2411.74,
    "sell_exchange": "Kraken",
    "sell_price": 2412.06,
    "spread_usd": 0.32,
    "spread_pct": 0.013,
    "timestamp": "2026-10-23 17:21:03 UTC"
  },
  {
    "pair": "SOL/USDT",
    "buy_exchange": "Kraken",
    "buy_price": 104.74,
    "sell_exchange": "Binance",
    "sell_price": 104.74,
    "spread_usd": 0.0,
    "spread_pct": 0.0,
    "timestamp": "2026-10-23 17:21:03 UTC"
  },
  {
    "pair": "XRP/USDT",
    "buy_exchange": "Binance",
    "buy_price": 1.3128,
    "sell_exchange": "Kraken",
    "sell_price": 1.31271,
    "spread_usd": -0.0,
    "spread_pct": -0.007,
    "timestamp": "2026-10-23 17:21:03 UTC"
  }
]
```

---

## 🛠️ Quickstart

```bash
git clone https://github.com/whyst0ne/crypto-arbitrage-scanner.git
cd crypto-arbitrage-scanner
pip install -r requirements.txt
python scanner.py
```

---

## 💳 x402 API & Direct Web3 Settlement
Autonomous agents and trading desks can settle per-call intelligence fees or sponsorships directly on-chain:

- **Multi-Chain EVM Wallet (Base / Arbitrum / Optimism / Polygon / Ethereum / Gnosis):**  
  `0xE5Ab26877172254B72f3AE6DA5789D2468B7B282`
- **Supported Settlement Tokens:** `USDC`, `USDT`, `DAI`, `ETH`
- **x402 Verification Header:** `X-Payment-TxHash: 0x...` (Verified on Base Mainnet USDC `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`)
