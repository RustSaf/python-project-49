#!/usr/bin/env python3
# game: gcd
import random
import math


INTRO = 'Find the greatest common divisor of given numbers.'


def game():
    num1, num2 = (random.randint(0, 100) for _ in range(2))
    question = f'{num1} {num2}'
    great_com_dev = str(math.gcd(num1, num2))
    return question, great_com_dev
