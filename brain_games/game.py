#!/usr/bin/env python3
# engine of games
from brain_games.cli import welcome_user


def engine_games(INTRO, game):
    name = welcome_user()
    print(INTRO)
    for _ in range(3):
        result = game()
        answer = input('Your answer: ')
        if answer == result:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
