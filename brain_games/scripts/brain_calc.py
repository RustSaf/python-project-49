#!/usr/bin/env python3
# script: calc
from brain_games.game import engine_games


def main():
    text_calc = 'What is the result of the expression?'
    engine_games(text_calc, 'calc')


if __name__ == '__main__':
    main()
