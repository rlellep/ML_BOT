import ccxt

exchange = ccxt.binance({
    'apiKey': '1v0OZcl24W9EqNRcQi1TdGMVzt7zwGNewUNSVFOlUwj2weaVCkxNHdz1nByBa1Tq',
    'secret': 'gWFhZwmkZKn0h1ftoEZbkDgUfXVV4r8egVPFHA1ZPQCswrG4L3kan1KM8eCg5nrr',
})

markets = exchange.load_markets()

with open('binance_available_pairs.txt', 'w') as f:
	f.writelines([i + '\n' for i in markets])