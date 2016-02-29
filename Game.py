'''
Game.py

An abstract base class that defines the attributes and methods
required for a game implementation such as a tile game, 8-puzzle, or
cannibal/missionary.

'''

from abc import ABCMeta # Metaclass required for creating an ABC.
import random

class Game(metaclass=ABCMeta):
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

class EightPuzzle(Game):
    tiles = set([0, 1, 2, 3, 4, 5, 6, 7, 8] # List of all tile values.
    start = {} # States in this game are dictionaries.
    goal = {0: set([2, 4, 6, 8]), # The goal dictionary.
            1: set([2, 8]),
            2: set([0, 1, 3]),
            3: set([2, 4]),
            4: set([0, 3, 5]),
            5: set([4, 6]),
            6: set([0, 5, 7]),
            7: set([6, 8]),
            8: set([0, 1, 7])}

    random.shuffle(tiles) # Shuffle tiles to generate random start state.

    for x in tiles: # Populate start dict randomly, ensuring legality.


    def __init__(self, graph, start, goal):
        Game.__init__(self, graph, start, goal)

