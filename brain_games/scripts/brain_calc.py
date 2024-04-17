#!/usr/bin/env python3
# script: calc
from brain_games.cli import welcome_user
from brain_games.game import engine_games


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    engine_games(name, 'calc')


if __name__ == '__main__':
    main()
