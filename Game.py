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
# Board tile numbering scheme
# 0 1 2
# 3 4 5
# 6 7 8


	tiles = [0, 1, 2, 3, 4, 5, 6, 7, 8] # List of all tile values.
	goal = (0, 1, 2, 4, 5, 6, 7, 8) # The goal dictionary.

	def __init__(self, graph, start, goal):
		Game.__init__(self, graph, start, goal)
		self.start = start # Start state is also the parent state.
		self.end = start # The graph state will be altered by Move().
		if(start == []):
			self.start = random.shuffle(tiles)
		print ('tiles ', tiles)
		else:
			self.start = start

		print ('Tiles: \n',tiles[0:3],'\n', tiles[3:6], '\n', tiles[6:9])
		print ('Start: ', start) 
		print ('Goal: ', goal)

	'''
		Method Move() attempts all possible moves for key 0 in the start
		dictionary and returns all graphs created from the moves. 
	'''
	def Move()
		children = []
		zeroindex = 0
		for i in len(start): # Create the start dictionary
			if graph[i] == 0:
				zeroindex = # Find the index of element 0.
		set_tuple = [] 
		if((zeroindex%3) > 0): # Link to the tile left on the gameboard.
			set_tuple.append(tiles[zeroindex-1])
		if ((zeroindex%3) < 2): # Link to the tile right on the gameboard.
			set_tuple.append(tiles[zeroindex+1])
		if (zeroindex > 2): # Link to the tile above on the gameboard. 
			set_tuple.append(tiles[zeroindex-3])
		if (zeroindex < 6): # Link to the tile below on the gameboard.
			set_tuple.append(tiles[zeroindex+3])
		# Update the dictionary with the new key, value pair.
		for j in len(set_tuple):
			graph = start
			temp = graph[i]
			graph[i] = graph[zeroindex]
			graph[zeroindex] = temp  
			children.append(graph)
		return start, children

