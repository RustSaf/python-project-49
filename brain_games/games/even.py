#!/usr/bin/env python3
# game: even
import random


INTRO = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return True if number % 2 == 0 else False


def get_question_and_right_answer():
    num = random.randint(0, 100)
    question = str(num)
    right_answer = 'yes' if is_even(num) else 'no'
    return question, right_answer
