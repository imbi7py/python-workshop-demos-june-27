#! /usr/bin/env python3
import random
import sys

# this is a comments

def main():
    if len(sys.argv) != 2:
        print("Error in randy. You must specify how many random numbers", file=sys.stderr)
        sys.exit(7)

    count = int(sys.argv[1])
    numbers = [str(random.randint(0, 1000)) for _ in range(count)]

    print(' '.join(numbers))


if __name__ == '__main__':
    main()
