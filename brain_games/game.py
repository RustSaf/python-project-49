#!/usr/bin/env python3
import brain_games.games.even
import brain_games.games.calc
import brain_games.games.gcd
import brain_games.games.progression
import brain_games.games.prime
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    print('This module is engine of the games.')


def engine_games(game):
    name = welcome_user()
    for _ in range(3):
        match game:
            case 'even':
                result = brain_games.games.even.main()
            case 'calc':
                result = brain_games.games.calc.main()
            case 'gcd':
                result = brain_games.games.gcd.main()
            case 'progression':
                result = brain_games.games.progression.main()
            case 'prime':
                result = brain_games.games.prime.main()
            case _:
                result = ''
        answer = input('Your answer: ')
        if answer == result:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
    return


if __name__ == '__main__':
    main()
