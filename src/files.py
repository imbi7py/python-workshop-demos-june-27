
# the text version
fin = open('stocks.csv', 'r')
text = fin.readlines()

for l in text[1:]:
    parts = [part for part in l.strip().split(',') if part]
    print(   'The symbol {} has volume {:,}.'.format(parts[0], int(parts[-1]))     )

fin.close()


with open('stocks.csv', 'r') as fin:
    fin.readline()
    for l in fin:
        parts = [part for part in l.strip().split(',') if part]
        print(   'The symbol {} has volume {:,}.'.format(parts[0], int(parts[-1]))     )


