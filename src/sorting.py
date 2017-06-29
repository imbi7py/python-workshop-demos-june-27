def find_numbers(lst, test):
    numbers = []
    for x in lst:
        if test(x):
            numbers.append(x)

    return numbers

def is_even(n):
    return n % 2 == 0

def is_big(n):
    return n > 500


numbers = [2, 1, 3, 4, 1000, 10001, 1002, 100, -5, -101, -1]
print(find_numbers(numbers, is_big))

def negate(n):
    return -n

def by_abs(n):
    return abs(n)

numbers.sort(key=by_abs)
print(numbers)

def get_value(m):
    return m[1]

measurements = [ (1, 5), (2, 3), (-1, 100)]
measurements.sort(key=get_value)
print(measurements)


print()
print()
print()

print(find_numbers(numbers, lambda n: n % 5 == 0))
measurements.sort(key=lambda m: -m[1])
print(measurements)



f = lambda x,y,z=5: print(x*y+z)

f(1,2)