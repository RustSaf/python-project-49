#!/usr/bin/env python3
# game: calc
import random


INTRO = 'What is the result of the expression?'


def get_question_and_right_answer():
    num1, num2 = (random.randint(0, 100) for _ in range(2))
    list_oper = ['+', '-', '*']
    oper = random.choice(list_oper)
    match oper:
        case '+':
            question = f'{num1} + {num2}'
            right_answer = str(num1 + num2)
        case '-':
            question = f'{num1} - {num2}'
            right_answer = str(num1 - num2)
        case '*':
            question = f'{num1} * {num2}'
            right_answer = str(num1 * num2)
    return question, right_answer
