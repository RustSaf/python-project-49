#!/usr/bin/env python3
# game: calc
import random


TEXT_CALC = 'What is the result of the expression?'


def intro():
    print(TEXT_CALC)


def calculate():
    num1, num2 = (random.randint(0, 100) for _ in range(2))
    i = random.randint(0, 2)
    match i:
        case 0:
            print(f'Question: {num1} + {num2}')
            calc = str(num1 + num2)
        case 1:
            print(f'Question: {num1} - {num2}')
            calc = str(num1 - num2)
        case _:
            print(f'Question: {num1} * {num2}')
            calc = str(num1 * num2)
    return calc
