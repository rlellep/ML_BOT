import ccxt
from datetime import datetime

#EDIT THESE PARAMETERS
stablecoin = 'USDT'
coins = ['BTC', 'ETH', 'DOGE'] #['BTC', 'ETH', 'BNB', 'XRP', 'DOGE', 'ADA', 'MATIC', 'DOT', 'LTC', 'SOL', 'UNI', 'AVAX', 'LINK', 'ATOM']
timeframes = ['5m', '15m']#['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
start_year = 2020
start_month = 1
start_day = 1
end_time = datetime.now()

exchange = ccxt.binance({
    'apiKey': '1v0OZcl24W9EqNRcQi1TdGMVzt7zwGNewUNSVFOlUwj2weaVCkxNHdz1nByBa1Tq',
    'secret': 'gWFhZwmkZKn0h1ftoEZbkDgUfXVV4r8egVPFHA1ZPQCswrG4L3kan1KM8eCg5nrr',
})
exchange.load_markets()

first_line = 'datetime_id, open, high, low, close, volume\n'
pairs = [coin + '/' + stablecoin for coin in coins]
timeframes_dict = {'1m': 60000, '5m': 300000, '15m': 900000, '30m': 1800000, '1h': 3600000, '4h': 14400000, '12h': 43200000, '1d': 86400000}
start_date = exchange.parse8601(f'{start_year}-{start_month:02}-{start_day:02} 00:00:00')
current_dateTime = exchange.parse8601(str(end_time)[:19])

for pair in pairs:
    for timeframe in timeframes:
        current_start_date = start_date
        data = []
        current_data = exchange.fetch_ohlcv(pair, timeframe=timeframe, since=current_start_date, limit=1000)
        data.extend([str(i)[1:-1] + '\n' for i in current_data])
        current_start_date = current_data[-1][0] + timeframes_dict[timeframe]
        this_coin_start_date = datetime.fromtimestamp(current_data[0][0]/1000)
        while len(current_data) % 1000 == 0 and current_start_date < current_dateTime - timeframes_dict[timeframe]:
            current_data = exchange.fetch_ohlcv(pair, timeframe=timeframe, since=current_start_date, limit=1000)
            data.extend([str(i)[1:-1] + '\n' for i in current_data])
            current_start_date = current_data[-1][0] + timeframes_dict[timeframe]

        data.insert(0, first_line)
        with open(f'data/{pair.replace("/", "-")}_{timeframe}_{this_coin_start_date.day:02}-{this_coin_start_date.month:02}-{this_coin_start_date.year}_{end_time.day:02}-{end_time.month:02}-{end_time.year}.csv', 'w') as f:
            f.writelines(data)