#! /usr/bin/env python3
import sys


def main():
    if len(sys.argv) <= 2:
        print("Error in randy. You must specify numbers to to multiply", file=sys.stderr)
        sys.exit(2)

    numbers = [int(num_text) for num_text in sys.argv[1:]]

    total = 1
    for n in numbers:
        total *= n

    print(total)


if __name__ == '__main__':
    main()
