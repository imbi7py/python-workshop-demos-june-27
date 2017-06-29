
numbers = [2, 3, 5, 7, 11, 13]

for n in numbers:
    print(n)
    print(n*n)
    print()


# greeting = input("Say something: ")
#
# while greeting != "bye":
#     print("You said " + greeting)
#     greeting = input("Say something: ")

while True:
    greeting = input("Say something: ")
    if greeting == 'shh':
        continue

    print("You said " + greeting)

    if greeting.lower().strip() == 'bye':
        break

print("Good bye")
