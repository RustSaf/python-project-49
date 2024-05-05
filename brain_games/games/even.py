#!/usr/bin/env python3
# game: even
import random


INTRO = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_remainder(number):
    return True if number % 2 == 1 else False


def game():
    num = random.randint(0, 100)
    question = str(num)
    answers = ['yes', 'no']
    even = answers[is_remainder(num)]
    return question, even
