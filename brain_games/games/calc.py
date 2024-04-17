#!/usr/bin/env python3
# game: calc
import random


def main():
    num1, num2 = (random.randint(0, 100) for _ in range(2))
    i = random.randint(0, 2)
    match i:
        case 0:
            print(f'Question: {num1} + {num2}')
            result = str(num1 + num2)
        case 1:
            print(f'Question: {num1} - {num2}')
            result = str(num1 - num2)
        case _:
            print(f'Question: {num1} * {num2}')
            result = str(num1 * num2)
    return result


if __name__ == '__main__':
    print(main())
