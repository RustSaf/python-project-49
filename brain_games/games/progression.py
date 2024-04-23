#!/usr/bin/env python3
# game: progression
import random


def main():
    num = random.randint(0, 100)
    step = random.randint(0, 10)
    progression = [str(num + step * i) for i in range(10)]
    random_index = random.randint(0, 9)
    lost_element = progression[random_index]
    progression[random_index] = '..'
    print('Question: ' + ' '.join(progression))
    return lost_element


if __name__ == '__main__':
    print(main())
