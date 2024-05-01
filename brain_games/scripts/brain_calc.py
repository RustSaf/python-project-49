#!/usr/bin/env python3
# script: calc
from brain_games.game import engine_games
from brain_games.games.calc import TEXT_CALC
from brain_games.games.calc import calculate


def main():
    engine_games(TEXT_CALC, calculate)
    return


if __name__ == '__main__':
    main()
