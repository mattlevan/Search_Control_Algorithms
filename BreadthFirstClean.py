'''

BreadthFirst search is a program that finds optimal solutions to games
(using the Game class) by iterating through all possible moves and
comparing to both the game goal state and all previous states visited.


'''
import Game
from EightPuzzle import EightPuzzle
from MissionaryCannibal import MissionaryCannibal
from SlidingTiles import SlidingTiles


class BreadthFirst:	

	def __init__(self, game):
		self.game = game
		self.goals = set()
		print('bfs created')


	'''
		buildGraph generates states and stores them in the graph{} 
		dictionary until either the goal is reached, or a set number
		of moves are performed.
	'''
	def buildGraph(self):
		MAX_MOVES = 10 # The max number of iterations before restarting.
		goalFound = False
		while not goalFound: # Generate nodes until goal is reached.
			start = self.game.gen_start()
			for gameGoal in self.game.goals:
				self.goals.add(gameGoal) 
			graph = {} # Stores visited states as (Parent, kids) pairs.

			# Get the initial move information for dictionary.
			parent, children = self.game.gen_moves(start)
			print('Parent: ', parent, ' Child: ',children)
			graph.update({parent: set(children)})
			print(graph)

			# For each key in the graph, add children to the dictionary
			# and check if a goal state is reached
			maxMoveCounter = 0
			# The game restarts if no goal is found in MAX_MOVES
			while maxMoveCounter < MAX_MOVES: 
				# Iterate through all keys and generate a dictionary
				# of new move states.
				tempGraph, goalFound = self.searchKeys(graph)
				# Update graph with the new moves stored in tempGraph.
				graph.update(tempGraph)
				maxMoveCounter += 1

		return self.game, graph	


	'''
		searchKeys searches through all child states for each parent
		key.  Child states not present as keys in the dictionary are
		added as new keys.  If a goal state has not yet been reached,
		child states are generated for the new keys.  Otherwise they
		are capped as and empty set().

	'''
	def searchKeys(self, searchGraph):

		goalFound = False
		graphKeys = searchGraph.keys()
		tempDict = {}
		# Iterate through every key in the graph. 
		for key in graphKeys:
			# Check that each path is present as a graph key.
			for vertex in searchGraph[key]:
				# If child state is not in graph, add it.
				if vertex not in searchGraph:
					# If the goal isn't reached, add new states.
					if not goalFound:
						# Generate child states and add to the graph.
						movestart, newstates = self.game.gen_moves(vertex)
						tempDict.update({movestart: set(newstates)})
					# If the goal was reached previously.
					else: 
						# Set all child states as an empty set
						tempDict.update({vertex: set()})
				# Compare the present vertex to the goal state.
				elif vertex in self.goals:
					goalFound = True
		return tempDict, goalFound


	'''
		bfs first calls buildGraph to generate a dictionary that
		has reached the goal state. The method then searches each state
		in the graph to find the shortest path to the goal. 

	'''
	def bfs(self):	
		# Generate a game and graph containing the goal state.
		legalGame, legalGraph = self.buildGraph()
		goalState = tuple(legalGame.goals)
		startState = legalGame.start
		# Store the states not yet visited in queue.
		queue = [(tuple(startState), [tuple(startState)])]
		# While the queue is not empty, perform the search.
		qcnt = 0
		while queue:
			qcnt += 1
			(vertex, path) = queue.pop(0) # Pop the current graph key.
			# For each child of a vertex/key compare to the states seen.
			# The subtraction leaves only unvisited paths in each key.
			cnt = 0
			for next in legalGraph[vertex] - set(path):
				cnt += 1
				# If already visited state, skip to next child state.
				if next in goalState:
					yield path + [next]
				else:
					queue.append((next, path + [next]))	


	'''
		shortestPath calls bfs (AKA the breadth first search function)
		and is meant to return all successful paths.
	'''
	def shortestPath(self):
		try:
			return next(self.bfs())
		except StopIteration:
			return None


'''
	All games and output format are run below.
'''

f = open("SearchResults.txt", 'w')
# Run the Eightpuzzle
eightGame = EightPuzzle()
bfsearch = BreadthFirst(eightGame)
eightSolutions = (bfsearch.shortestPath())
strSolutions = str(eightSolutions)
f.write(('EightPuzzle path to success \nStart:'))
moveCount = 0
for state in eightSolutions:
	f.write(('\nMove '+str(moveCount)+'\n'+str(state[0:3])+'\n' + str(state[3:6])+'\n'+str(state[6:9])))
	moveCount += 1

missionGame = MissionaryCannibal()
bfSearchMission = BreadthFirst(missionGame)
missionSolutions = (bfSearchMission.shortestPath())
f.write(('\n\nMissionary Path to success \nStart:'))
moveCount = 0
for state in missionSolutions:
	f.write(('\nMove '+str(moveCount)+str(state)))
	moveCount += 1

tileGame = SlidingTiles()
bfSearchTiles = BreadthFirst(tileGame)
tileSolutions = (bfSearchTiles.shortestPath())
f.write(('\n\nSliding Tiles Path to success \nStart:'))
moveCount = 0
for state in tileSolutions:
	f.write(('\nMove '+str(moveCount)+str(state)))
	moveCount += 1
# Close output file
f.close()


