import ccxt
import time
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "exchanges": ["kraken", "bybit", "kucoin", "gate", "bitget"],
        "pairs": ["BTC/USDT", "ETH/USDT", "SOL/USDT", "XRP/USDT", "DOGE/USDT"],
        "taker_fee": 0.001,
        "min_profit_pct": 0.05,
        "output_file": "arbitrage_signals.json"
    }

def main():
    cfg = load_config()
    exchanges = {}
    for name in cfg["exchanges"]:
        try:
            ex_cls = getattr(ccxt, name)
            exchanges[name] = ex_cls({'enableRateLimit': True, 'timeout': 10000})
        except Exception as e:
            print(f"[!] Warning: Failed to load exchange {name}: {e}")

    print(f"[*] Scanning {len(cfg['pairs'])} pairs across {len(exchanges)} exchanges...")
    prices = {ex: {} for ex in exchanges}

    for ex_name, ex in exchanges.items():
        for pair in cfg["pairs"]:
            try:
                t = ex.fetch_ticker(pair)
                if t.get('bid') and t.get('ask'):
                    prices[ex_name][pair] = {'bid': t['bid'], 'ask': t['ask']}
            except Exception:
                pass
            time.sleep(0.1)

    signals = []
    for pair in cfg["pairs"]:
        best_bid = {'exchange': None, 'price': 0}
        best_ask = {'exchange': None, 'price': float('inf')}

        for ex_name in exchanges:
            data = prices.get(ex_name, {}).get(pair)
            if not data:
                continue
            if data['bid'] > best_bid['price']:
                best_bid = {'exchange': ex_name, 'price': data['bid']}
            if data['ask'] < best_ask['price']:
                best_ask = {'exchange': ex_name, 'price': data['ask']}

        if best_bid['exchange'] and best_ask['exchange'] and best_bid['exchange'] != best_ask['exchange']:
            spread = (best_bid['price'] - best_ask['price']) / best_ask['price']
            net = (spread - (2 * cfg['taker_fee'])) * 100
            print(f"[{pair}] Buy: {best_ask['exchange']} (${best_ask['price']:.4f}) -> Sell: {best_bid['exchange']} (${best_bid['price']:.4f}) | Spread: {spread*100:+.3f}% | Net: {net:+.3f}%")
            if net >= cfg['min_profit_pct']:
                signals.append({
                    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                    'pair': pair,
                    'buy_exchange': best_ask['exchange'],
                    'buy_price': best_ask['price'],
                    'sell_exchange': best_bid['exchange'],
                    'sell_price': best_bid['price'],
                    'gross_spread_pct': round(spread * 100, 3),
                    'net_profit_pct': round(net, 3)
                })

    if signals:
        print(f"[+] Found {len(signals)} profitable signals!")
        with open(cfg.get("output_file", "arbitrage_signals.json"), "w", encoding="utf-8") as f:
            json.dump(signals, f, indent=2)

if __name__ == "__main__":
    main()
