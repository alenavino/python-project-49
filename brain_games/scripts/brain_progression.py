#!/usr/bin/env python3


from brain_games.scripts.brain_games import greet
from brain_games.engine import engine
from brain_games.games.progression import progression


def main():
    greet()
    engine(progression)


if __name__ == '__main__':
    main()
