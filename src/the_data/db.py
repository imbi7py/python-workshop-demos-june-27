import sqlite3

connect_string = 'image.sqlite'
# connect_string = 'image.bin'

conn = sqlite3.connect(connect_string)
results = conn.execute("SELECT * FROM Episodes WHERE show_id > 3 AND title like '%3.6%'")
# print(type(results))

for r in results:
    print("Show {} is {}".format(r[1], r[2]))

conn.close()
