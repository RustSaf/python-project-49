#!/usr/bin/env python3
# script: prime
from brain_games.game import engine_games
from brain_games.games.prime import TEXT_PRIME
from brain_games.games.prime import prime_num


def main():
    engine_games(TEXT_PRIME, prime_num)
    return


if __name__ == '__main__':
    main()
