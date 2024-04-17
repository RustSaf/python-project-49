#!/usr/bin/env python3
# script: even
from brain_games.cli import welcome_user
from brain_games.game import engine_games


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    engine_games(name, 'even')


if __name__ == '__main__':
    main()
