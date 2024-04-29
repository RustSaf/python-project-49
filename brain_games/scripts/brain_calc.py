#!/usr/bin/env python3
# script: calc
from brain_games.cli import welcome_user
from brain_games.game import engine_games
from brain_games.games.calc import intro
from brain_games.games.calc import calculate


def main():
    name = welcome_user()
    intro()
    status = True
    count = 0
    max = 3
    while status:
        if count != max:
            status = engine_games(name, calculate(), True)
        else:
            status = engine_games(name, '', False)
        count += 1
    return


if __name__ == '__main__':
    main()
