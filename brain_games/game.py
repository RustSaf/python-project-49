#!/usr/bin/env python3
import games


def main():
    print('Welcome to the Brain Games!')
    print('This module is engine of the games.')


def engine_games(name, game):
    for _ in range(3):
        match game:
            case 'even':
                result = games.even()
            case 'calc':
                result = games.calc()
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


if __name__ == '__main__':
    main()
