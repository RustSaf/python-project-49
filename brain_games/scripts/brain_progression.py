#!/usr/bin/env python3
# script: progression
from brain_games.game import engine_games
from brain_games.games.progression import TEXT_PROGRESSION
from brain_games.games.progression import progress


def main():
    engine_games(TEXT_PROGRESSION, progress)
    return


if __name__ == '__main__':
    main()
