#!/usr/bin/env python3
# game: prime
import random


TEXT_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_remain(number):
    for i in range(2, number):
        remain = number % i
        if remain == 0:
            return 1
    return 0


def prime_num():
    num = random.randint(3, 100)
    print(f'Question: {num}')
    answers = ['yes', 'no']
    prime = answers[is_remain(num)]
    return prime
