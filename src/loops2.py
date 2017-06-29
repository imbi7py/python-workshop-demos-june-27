


fibs = [1,1,2,3,5,8,13,21]

for n in fibs:
    print(n, end=' | ')
print()
print()

for idx in range(len(fibs)):
    print("The {}th fib num is {}".format(idx+1, fibs[idx]))

for idx, value in enumerate(fibs):
    print("The {}th fib num is {}".format(idx + 1, value))


idx, value = (2,5)
print(idx)
print(value)

# for x in type(""):
#     print(x)


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __iter__(self):
        return self.items.__iter__()

cart = ShoppingCart()
cart.add_item("Car")
cart.add_item("CD")
cart.add_item("Pillow")


for item in cart:
    print(item)












