#!/usr/bin/env python3
# game: gcd
import random
import math


TEXT_GCD = 'Find the greatest common divisor of given numbers.'


def greate_com_dev():
    num1, num2 = (random.randint(0, 100) for _ in range(2))
    print(f'Question: {num1} {num2}')
    gcd = str(math.gcd(num1, num2))
    return gcd
