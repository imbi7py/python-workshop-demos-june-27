import os
import csv
import json
import collections

Stock = collections.namedtuple('Stock', 'symbol,open,high,low,close,volume')

folder = os.path.dirname(__file__)
csv_file = os.path.join(folder, 'reports', 'stocks.csv')

with open(csv_file, 'r') as fin:
    data = csv.DictReader(fin)

    for row in data:
        stock = Stock(**row)
        print('The symbol {} has volume {:,}.'.format(stock.symbol, int(stock.volume)))


with open(csv_file, 'r') as fin:
    data = csv.DictReader(fin)

    # Stocks over 200 on close
    high_stocks = [
        Stock(**row)
        for row in data # set to pull from
        if float(row.get('close', -1)) > 200  # test condition for inclusion
    ]

high_stocks.sort(key=lambda s: -float(s.high))
print(high_stocks)

to_save_data = [
    {
        'symbol': h.symbol,
        'high': float(h.high),
        'volume': int(h.volume)
    }
    for h in high_stocks
]
print(to_save_data)

with open("reports\\stocks.json", 'w') as fout:
    json.dump(to_save_data, fout, indent=True)



with open("reports\\stocks.json", 'r') as fin:
    data = json.load(fin)
    for stock in data:
        print(stock.get('symbol'), stock.get('volume'))








