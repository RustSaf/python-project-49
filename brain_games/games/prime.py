#!/usr/bin/env python3
# game: prime
import random


INTRO = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_remainder(number):
    for i in range(2, number):
        remain = True if number % i > 0 else False
        if remain is False:
            return remain
        else:
            continue
    return remain


def game():
    num = random.randint(3, 100)
    question = str(num)
    answers = ['no', 'yes']
    prime = answers[is_remainder(num)]
    return question, prime
