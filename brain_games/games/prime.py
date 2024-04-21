#!/usr/bin/env python3
# game: prime
import random


def main():
    num = random.randint(0, 100)
    print(f'Question: {num}')
    answers = ['no', 'yes']
    for i in range(2, num):
        remain = num % i
        if remain == 0:
            prime = answers[0]
            return prime
        else:
            prime = answers[1]
    return prime


if __name__ == '__main__':
    print(main())
