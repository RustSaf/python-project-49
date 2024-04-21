#!/usr/bin/env python3
# script: gcd
from brain_games.cli import welcome_user
from brain_games.game import engine_games


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    engine_games(name, 'gcd')


if __name__ == '__main__':
    main()
