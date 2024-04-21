#!/usr/bin/env python3
# script: prime
from brain_games.cli import welcome_user
from brain_games.game import engine_games


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    engine_games(name, 'prime')


if __name__ == '__main__':
    main()
