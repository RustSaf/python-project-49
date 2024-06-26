#!/usr/bin/env python3
# engine of games
from brain_games.cli import welcome_user


MAX_COUNT = 3


def engine_games(game):
    name = welcome_user()
    print(game.INTRO)
    for _ in range(MAX_COUNT):
        question, result = game.get_question_and_right_answer()
        print('Question: ' + question)
        answer = input('Your answer: ')
        if answer == result:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
