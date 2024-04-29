#!/usr/bin/env python3
# engine of games


def engine_games(name, result, action):
    while action:
        answer = input('Your answer: ')
        if answer == result:
            print('Correct!')
            return True
        else:
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return False
    print(f'Congratulations, {name}!')
