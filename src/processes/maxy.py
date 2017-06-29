#! /usr/bin/env python3
import sys


def main():
    if len(sys.argv) <= 2:
        print("Error in randy. You must specify how many numbers to keep and the number list", file=sys.stderr)
        sys.exit(5)

    count = int(sys.argv[1])
    numbers = [int(num_text) for num_text in sys.argv[2:]]
    numbers.sort()

    selected_text = [str(n) for n in numbers[-count:]]
    print(' '.join(selected_text))


if __name__ == '__main__':
    main()
