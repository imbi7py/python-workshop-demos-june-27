import random
import other
from other import size
size = 3

print("Other's size: {}".format(size))
print("My size: {}".format(size))

# heads = 0
# tails = 1
# the_flip = random.randint(0, 1)

def main():
    the_flip = flip_coin()
    the_guess = get_input_from_user()
    decide_winner(the_flip, the_guess)

def flip_coin():
    print("flipping coin...")
    return random.choice( ['heads', 'tails'] )

# def flip_coin():
#     print("Other flip")
#     return 'cats'


def get_input_from_user():
    return input('heads or tails? ')

def print_result(the_guess, the_flip):

    print("The flip: {}".format(the_flip))
    print("The guess: {}".format(the_guess))


def decide_winner(the_flip, the_guess):
    if check_has_won(the_flip, the_guess):
        print("Yay, you win!")
        print("Nice work. You guessed {} and it was {}".format(the_guess, the_flip))
    else:
        print("Sorry, you lost")

def check_has_won(coin, guess):
    return coin == guess

def other_function(x=0, y=0, z=1, *args, **kwargs):
    print(x, y, z, args, kwargs)

other_function(1, 2, z=7, alpha=.2, mode=True)


##################################
import collections
UserInfo = collections.namedtuple('UserInfo', 'name, id')

def get_user_info():
    name = 'michael'
    id = 42

    return UserInfo(name, id)


info = get_user_info()
user, the_id = get_user_info()
print("The user info: {}, {}".format(the_id, user))
##################################



if __name__ == '__main__':
    main()
