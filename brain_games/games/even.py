#!/usr/bin/env python3
# game: even
import random


def main():
    num = random.randint(0, 100)
    print(f'Question: {num}')
    answers = ['yes', 'no']
    i = num % 2
    even = answers[i]
    return even


if __name__ == '__main__':
    print(main())
