#!/usr/bin/env python3
# script: prime
from brain_games.cli import welcome_user
from brain_games.game import engine_games
from brain_games.games.prime import intro
from brain_games.games.prime import prime_num


def main():
    name = welcome_user()
    intro()
    status = True
    count = 0
    max = 3
    while status:
        if count != max:
            status = engine_games(name, prime_num(), True)
        else:
            status = engine_games(name, '', False)
        count += 1
    return


if __name__ == '__main__':
    main()
