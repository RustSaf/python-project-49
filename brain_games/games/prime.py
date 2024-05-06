#!/usr/bin/env python3
# game: prime
import random


INTRO = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for i in range(2, number):
        remain = True if number % i > 0 else False
        if remain is False:
            return remain
        else:
            continue
    return remain


def get_question_and_right_answer():
    num = random.randint(3, 100)
    question = str(num)
    right_answer = 'yes' if is_prime(num) else 'no'
    return question, right_answer
