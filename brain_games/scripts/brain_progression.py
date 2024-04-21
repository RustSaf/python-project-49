#!/usr/bin/env python3
# script: progression
from brain_games.cli import welcome_user
from brain_games.game import engine_games


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    engine_games(name, 'progression')


if __name__ == '__main__':
    main()
