#!/usr/bin/env python3
# game: progression
import random


INTRO = 'What number is missing in the progression?'


def get_question_and_right_answer():
    num = random.randint(0, 100)
    step = random.randint(0, 10)
    progression = [str(num + step * i) for i in range(10)]
    random_index = random.randint(0, 9)
    right_answer = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(progression)
    return question, right_answer
