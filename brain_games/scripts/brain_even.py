#!/usr/bin/env python3
# script: even
from brain_games.game import engine_games
from brain_games.games.even import TEXT_EVEN
from brain_games.games.even import parity


def main():
    engine_games(TEXT_EVEN, parity)
    return


if __name__ == '__main__':
    main()
