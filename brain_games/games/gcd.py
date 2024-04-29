#!/usr/bin/env python3
# game: gcd
import random


TEXT_GCD = 'Find the greatest common divisor of given numbers.'


def intro():
    print(TEXT_GCD)


def greate_com_dev():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f'Question: {num1} {num2}')
    a = max(num1, num2)
    b = min(num1, num2)
    remind = a % b
    gcd = str(b)
    while remind != 0:
        a = b
        b = remind
        remind = a % b
        gcd = str(b)
    return gcd
