'''
Game.py

An abstract base class that defines the attributes and methods
required for a game implementation such as a tile game, 8-puzzle, or
cannibal/missionary.

'''

#from abc import ABCMeta # Metaclass required for creating an ABC.
import random

#class Game_list(metaclass=ABCMeta):
#	def __init__(self, start):
#		self.start = start

class EightPuzzle:
# Board tile numbering scheme
# 0 1 2
# 3 4 5
# 6 7 8
	def __init__(self, start):
		self.goal = [0,1,2,3,4,5,6,7,8]
		if(start == []):
			print('Start is empty')
			self.start = [0,1,2,3,4,5,6,7,8]
			random.shuffle(self.start)
			print('self.start = ', self.start)
		else:
			self.start = list(start)
	'''
		Method Move() attempts all possible moves for key 0 in the start
		dictionary and returns all lists created from the moves. 
	'''
	def Move(self, start_state): 
		self.children = []
		self.zeroindex = 0
		move_index = [] # Stores the index  of each possible move.
		for i in range(len(start_state)): 
			if self.start[i] == 0:
				self.zeroindex = i # Find the index of element 0.
		if((self.zeroindex%3) > 0): # Find the left board tile index.
			move_index.append(self.zeroindex-1)
		if ((self.zeroindex%3) < 2): # Find the right board tile index.
			move_index.append(self.zeroindex+1)
		if (self.zeroindex > 2): # Find the upper board tile index.
			move_index.append(self.zeroindex-3)
		if (self.zeroindex < 6): # Find the lower board tile index.
			move_index.append(self.zeroindex+3)
		print('Possible moves: ', move_index)
		for j in move_index: # Generate all children with 0 tile swap.
			move = list(start_state)
			temp = move[j]
			print('Tile being swapped with 0: ', temp)
			move[j] = move[self.zeroindex]
			print('Moved 0 tile to index ',j,' = ',move[self.zeroindex])
			move[self.zeroindex] = temp  
			self.children.append(move)
			print('Children: ', self.children)
		return tuple(start_state), self.children
	
	def GetStart(self):
		return self.start
	
	def GetGoal(self):
		return self.goal
