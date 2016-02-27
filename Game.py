'''
Game.py

An abstract base class that defines the attributes and methods
required for a game implementation such as a tile game, 8-puzzle, or
cannibal/missionary.

'''

from abc import ABCMeta # Metaclass required for creating an ABC.

class Game(metaclass=ABCMeta):
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
