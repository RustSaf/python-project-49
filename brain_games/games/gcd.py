#!/usr/bin/env python3
# game: gcd
import random


def main():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f'Question: {num1} {num2}')
    a = max(num1, num2)
    b = min(num1, num2)
    remind = a % b
    gcd = str(b)
    while remind != 0:
        a = b
        b = remind
        remind = a % b
        gcd = str(b)
    return gcd


if __name__ == '__main__':
    print(main())
