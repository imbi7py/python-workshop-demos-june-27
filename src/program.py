import datetime

# Capture start time
t0 = datetime.datetime.now()
# print(t0)

x = 7
y = 11

z = x * y
print(z, x, y)

name = "Michael"
saying = "Hello "

greeting = saying + name
print(greeting)

greeting = z+1
print(greeting)

# capture end time
t1 = datetime.datetime.now()
dt = t1 - t0

print(dt.total_seconds())
