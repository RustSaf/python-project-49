#!/usr/bin/env python3
# game: gcd
import random


def main():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    print(f'Question: {num1} {num2}')
    if num1 == 0 and num2 == 0:
        return 0
    elif num1 != num2 and (num1 == 0 or num2 == 0):
        return "This is exception!"
    else:
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
