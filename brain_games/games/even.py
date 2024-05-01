#!/usr/bin/env python3
# game: even
import random


TEXT_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    remain = number % 2
    return remain


def parity():
    num = random.randint(0, 100)
    print(f'Question: {num}')
    answers = ['yes', 'no']
    even = answers[is_even(num)]
    return even
