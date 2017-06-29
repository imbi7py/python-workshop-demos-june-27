import collections

Stock = collections.namedtuple('Stock', 'symbol, open, high, low, close, volume')

stocks = [
    Stock('AAL', 49, 49.1, 48.47, 48.63, 11901883),
    Stock('AAPL', 145.13, 147.16, 145.11, 146.28, 33917635),
    Stock('ADBE', 143.75, 145.59, 143.06, 145.41, 3383524),
    Stock('AMZN', 1002.54, 1004.62, 998.02, 1003.74, 2832807),
    Stock('GOOGL', 975.5, 986.62, 974.46, 986.09, 1524905),
    Stock('MAT', 20.22, 20.75, 20.11, 20.68, 10603967),
    Stock('MSFT', 70.09, 71.25, 69.92, 71.21, 26803888),
    Stock('NTES', 320, 333.78, 319, 333.56, 1356386),
]


high_stocks = []
for s in stocks:
    if s.high > 200:
        res = (s.symbol, s.high)
        high_stocks.append(res)

print(high_stocks)

high_stocks = [
    (s.symbol, s.high) # the item to place in the list
    for s in stocks # loop over the items
    if s.high > 200 # test for inclusion
]


high_stocks = [(s.symbol, s.high) for s in stocks if s.high > 200]
print(high_stocks)

print("average close:")
print(       sum( [s.close for s in stocks] ) / len(stocks)                   )


total = 0
for s in stocks:
    total += s.close
ave = total / len(stocks)
print(ave)


print("Max close")
print(max([s.close for s in stocks]))

closes = [s.close for s in stocks]
print(type(closes), closes)

closes_lookup = {
    s.symbol : s.close
    for s in stocks
}
print(type(closes_lookup), closes_lookup)

print(closes_lookup.get('GOOGL'))

s = set()
s.add('appl')
s.add('googl')
s.add('googl')
s.add('googl')
s.add('googl')
s.add('googl')
print(s)

symbols = {
    s.symbol
    for s in stocks
}
print(type(symbols), symbols)
print('MSFT' in symbols)
print('IBM' in symbols)


high_stocks_g = (
    (s.symbol, s.high) # the item to place in the list
    for s in stocks # loop over the items
    if s.high > 200 # test for inclusion
)

print(list(high_stocks_g))
print(type(high_stocks_g), high_stocks_g)
print("Running")
for s in high_stocks_g:
    print(s)
print("Running")
for s in high_stocks_g:
    print(s)
print("Running")
for s in high_stocks_g:
    print(s)









