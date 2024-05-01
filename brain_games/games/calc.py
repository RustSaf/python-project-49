#!/usr/bin/env python3
# game: calc
import random


TEXT_CALC = 'What is the result of the expression'


def calculate():
    num1, num2 = (random.randint(0, 100) for _ in range(2))
    list_oper = ['+', '-', '*']
    oper = random.choice(list_oper)
    match oper:
        case '+':
            print(f'Question: {num1} + {num2}')
            calc = str(num1 + num2)
        case '-':
            print(f'Question: {num1} - {num2}')
            calc = str(num1 - num2)
        case '*':
            print(f'Question: {num1} * {num2}')
            calc = str(num1 * num2)
    return calc
