#!/usr/bin/env python3
# game: prime
import random


TEXT_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def intro():
    print(TEXT_PRIME)


def prime_num():
    num = random.randint(3, 100)
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
