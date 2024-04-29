#!/usr/bin/env python3
# game: even
import random


TEXT_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'


def intro():
    print(TEXT_EVEN)


def parity():
    num = random.randint(0, 100)
    print(f'Question: {num}')
    answers = ['yes', 'no']
    i = num % 2
    even = answers[i]
    return even
