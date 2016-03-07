'''

BreadthFirst search is a program that finds optimal solutions to games
(using the Game class) by iterating through all possible moves and
comparing to both the game goal state and all previous states visited.


'''
from Game_list import EightPuzzle

class BreadthFirst:	
	'''
		buildGraph generates states and stores them in the graph{} 
		dictionary until either the goal is reached, or a set number
		of moves are performed.
	'''
	def __init__(self, game):
		self.game = game
		print('bfs created')

	def buildGraph(self):
		MAX_MOVES = 1 
		goalFound = False
		while not goalFound:
			start = [1,2,3,8,0,4,7,6,5]#self.game.GetStart()
			goal = tuple(self.game.GetGoal())
			# Generate a new game and get the start/goal states.
			self.game = EightPuzzle(start) 
			graph = {} # Stores visited states as (Parent, children) pairs.
			# Get the initial move information for dictionary.
			parent, children = self.game.Move(start)
			print('Parent: ', parent, ' Child: ',children)
			graph.update({parent: set(children)})
			# For each key in the graph, add children to the dictionary
			# and check if a goal state is reached
			counter = 0
			while counter < MAX_MOVES: 
				tempdict = {}
				graphKeys = graph.keys() # Get a list of all keys.
#				print('graphKeys: ', graphKeys)
				loopcounter = 0
				for key in graphKeys: # Iterate through each key in graph.
					loopcounter += 1
					print('Total Keys', len(graphKeys), 'loop# ', loopcounter)
					# Check that each path is present as a graph key.
					for vertex in graph[key]:
						if vertex not in graph:
							# If the goal isn't reached, add new states.
							if not goalFound:
								movestart, newstates = self.game.Move(vertex)
								tempdict.update({movestart: set(newstates)})
								print('Tempdict size: ', len(tempdict))
							# If the goal was found, add the key without
							# a connection to new states.
							else: 
								print('vertex capped as set(): ', vertex)
								tempdict.update({vertex: set()})
						elif vertex == goal:
					#		print('goal found!')
							goalFound = True
				graph.update(tempdict)
				print('updating dictionary')
				print('Size of dictionary', len(graph))
				if goal in graph:
					print('Goal found!')
					goalFound = True
				counter += 1
		print('Verify all keys found: ')
		for key in graph:
			for vertex in graph[key]:
				if vertex not in graph:
					print('Key ', vertex, ' not found')	
		print('goalFound: ', goalFound)
#		print('dictionary: ', graph)
		return self.game, graph	
	'''
		bfs first calls buildGraph to generate a dictionary that
		has reached the goal state. The method then searches each state
		in the graph to find the shortest path to the goal. 

	'''
	def bfs(self):	
		# Generate a game and graph containing the goal state.
		legalGame, legalGraph = self.buildGraph()
		goalState = tuple(legalGame.GetGoal())
		startState = legalGame.GetStart()
		# Store the states not yet visited in queue.
		queue = [(tuple(startState), [tuple(startState)])]
		# While the queue is not empty, perform the search.
		while queue:
			(vertex, path) = queue.pop(0) # Pop the current graph key.
#j			print('vertex: ', vertex,' is in graph?: ', vertex in legalGraph)
#			print('graph[', vertex, ']: ', legalGraph[vertex])		
#			print('queue: ', queue, ' vertex: ', vertex, ' path: ', path)
			# For each child of a vertex/key compare to the states seen.
			for next in legalGraph[vertex] - set(path):
				print('Next1: ', next, ' Goal: ', goalState, ' equal?', next == goalState)
				# If already visited state, skip to next child state.
				if next == goalState:
					print('Goal found, path+[next]:\n', path+[next])
					yield path + [next]
				else:
					queue.append((next, path + [next]))	
					print('appending: ', next)


	def shortestPath(self):
		try:
			return next(self.bfs())
		except StopIteration:
			return None

newgame = EightPuzzle([])
bfsearch = BreadthFirst(newgame)
list1 = list(bfsearch.shortestPath())
print('Path to success: ')
for i, x in list1, range(len(list1)):
	print('\nMove ', x, ':\n', i[0:3], '\n', i[3:6], '\n', i[6:9])


