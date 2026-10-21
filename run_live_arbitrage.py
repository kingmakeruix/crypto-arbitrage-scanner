import urllib.request
import json
import time

def fetch_binance(symbol):
    try:
        url = f"https://api.binance.com/api/v3/ticker/bookTicker?symbol={symbol}"
        req = urllib.request.Request(url, headers={'User-Agent': 'ArbitrageEngine/2.0'})
        with urllib.request.urlopen(req, timeout=5) as r:
            data = json.loads(r.read().decode())
            return {
                "bid": float(data['bidPrice']),
                "ask": float(data['askPrice'])
            }
    except Exception as e:
        return None

def fetch_kraken(pair):
    try:
        url = f"https://api.kraken.com/0/public/Ticker?pair={pair}"
        req = urllib.request.Request(url, headers={'User-Agent': 'ArbitrageEngine/2.0'})
        with urllib.request.urlopen(req, timeout=5) as r:
            data = json.loads(r.read().decode())
            key = list(data['result'].keys())[0]
            item = data['result'][key]
            return {
                "bid": float(item['b'][0]),
                "ask": float(item['a'][0])
            }
    except Exception as e:
        return None

def fetch_coinbase(product):
    try:
        url = f"https://api.exchange.coinbase.com/products/{product}/ticker"
        req = urllib.request.Request(url, headers={'User-Agent': 'ArbitrageEngine/2.0'})
        with urllib.request.urlopen(req, timeout=5) as r:
            data = json.loads(r.read().decode())
            return {
                "bid": float(data['bid']),
                "ask": float(data['ask'])
            }
    except Exception as e:
        return None

pairs_map = [
    {"name": "BTC/USDT", "binance": "BTCUSDT", "kraken": "XBTUSDT", "coinbase": "BTC-USDT"},
    {"name": "ETH/USDT", "binance": "ETHUSDT", "kraken": "ETHUSDT", "coinbase": "ETH-USDT"},
    {"name": "SOL/USDT", "binance": "SOLUSDT", "kraken": "SOLUSDT", "coinbase": "SOL-USDT"},
    {"name": "XRP/USDT", "binance": "XRPUSDT", "kraken": "XRPUSDT", "coinbase": None}
]

print("=== REAL-TIME MULTI-EXCHANGE ARBITRAGE SCANNER ===")
timestamp = time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())
print(f"Timestamp: {timestamp}\n")

opportunities = []

for p in pairs_map:
    quotes = {}
    if p["binance"]:
        q = fetch_binance(p["binance"])
        if q: quotes["Binance"] = q
    if p["kraken"]:
        q = fetch_kraken(p["kraken"])
        if q: quotes["Kraken"] = q
    if p["coinbase"]:
        q = fetch_coinbase(p["coinbase"])
        if q: quotes["Coinbase"] = q

    if len(quotes) >= 2:
        # Find best buy (lowest ask) and best sell (highest bid)
        best_buy_ex = min(quotes.keys(), key=lambda ex: quotes[ex]["ask"])
        best_buy_price = quotes[best_buy_ex]["ask"]

        best_sell_ex = max(quotes.keys(), key=lambda ex: quotes[ex]["bid"])
        best_sell_price = quotes[best_sell_ex]["bid"]

        spread = best_sell_price - best_buy_price
        pct = (spread / best_buy_price) * 100

        print(f"[{p['name']}] Quotes: " + ", ".join([f"{ex}: Bid={q['bid']:.2f}/Ask={q['ask']:.2f}" for ex, q in quotes.items()]))
        print(f"  Best Route: BUY on {best_buy_ex} (${best_buy_price:.2f}) -> SELL on {best_sell_ex} (${best_sell_price:.2f})")
        print(f"  Gross Spread: ${spread:.2f} ({pct:+.3f}%)\n")

        opportunities.append({
            "pair": p["name"],
            "buy_exchange": best_buy_ex,
            "buy_price": best_buy_price,
            "sell_exchange": best_sell_ex,
            "sell_price": best_sell_price,
            "spread_usd": round(spread, 2),
            "spread_pct": round(pct, 3),
            "timestamp": timestamp
        })

with open("arbitrage_live_signals.json", "w", encoding="utf-8") as f:
    json.dump(opportunities, f, indent=2)

print(f"Saved {len(opportunities)} live arbitrage evaluations to arbitrage_live_signals.json.")
