import beautifulsoup4
import validus
import datetime

def func(x, y):
    pass


try:
    guess = input("Enter a number")
    guess = int(guess)
    print("That worked.")
except Exception as x:
    print("That didn't work!")
    print(x)

print("Didn't crash")

guess = input("Enter a number")
if validus.isint(guess):
    guess = int(guess)
else:
    print("Must be a number")


func()