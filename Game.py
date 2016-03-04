'''
Game.py

An abstract base class that defines the attributes and methods
required for a game implementation such as a tile game, 8-puzzle, or
cannibal/missionary.

'''

import random

class Game:
    start, goal = []

    def __init__(self, start, goal):
        if type(start) is []:
            self.start = start
        else:
            print('Game requires start state to be a list.')
            exit(1)
        if type(goal) is []:
            self.goal = goal
        else:
            print('Game requires goal state to be a list.')
            exit(1)
