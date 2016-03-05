'''

BreadthFirst search is a program that finds optimal solutions to games
(using the Game class) by iterating through all possible moves and
comparing to both the game goal state and all previous states visited.


'''
from Game_list import EightPuzzle

class BreadthFirst:	
	'''
		build_graph generates states and stores them in the graph{} 
		dictionary until either the goal is reached, or a set number
		of moves are performed.
	'''

	def __init__(self):
		print('bfs created')

	def build_graph(self):
		MAX_MOVES = 300
		goal_found = False
		while not goal_found:
			# Generate a new game and get the start/goal states.
			puzzle = EightPuzzle([]) 
			start = puzzle.GetStart()
			goal = tuple(puzzle.GetGoal())
			graph = {} # Stores visited states as (Parent, children) pairs.
			# Get the initial move information for dictionary.
			parent, children = puzzle.Move(start)
			graph.update({parent: children})
			# For each key in the graph, add children to the dictionary
			# and check if a goal state is reached
			key = parent 
			tempdict = {}
			counter = 0
			while counter < MAX_MOVES: 
				for key in graph:
					for vertex in graph[key]:
						child = tuple(vertex)
						print('child: ',child, ' vertex: ',vertex, '\nkey: ', key, 'graph[key]: ', graph[key])
						# If the child is not in the dictionary, add it.
						if child not in graph:
							movestart, newstates = puzzle.Move(child)
							print('movestart: ',movestart, ' states: ',newstates)
							tempdict.update({movestart: newstates})
					#print('key: ', key)
				# If the goal is reached, set the goal_found boolean.
				graph.update(tempdict)
				print('updating dictionary')
				for key in graph:
					print(key)
				if goal in graph:
					print('Goal found!')
					goal_found = True
					break
				counter += 1
		return puzzle, graph	
	'''
		bfs first calls build_graph to generate a dictionary that
		has reached the goal state. The method then searches each state
		in the graph to find the shortest path to the goal. 

	'''
	def bfs(self):	
		# Generate a game and graph containing the goal state.
		legal_game, legal_graph = self.build_graph()
		goal_state = legal_game.GetGoal()	
		# Store the states not yet visited in queue.
		visited, queue = set(), legal_game.GetStart() 
		
		# While the queue is not empty, perform the search.
		while queue:
			(vertex, path) = queue.pop(0) # Pop the current graph key.
			
			# For each child of a vertex/key compare to the states seen.
			for next in graph[vertex]:
				# If already visited state, skip to next child state.
				if next in path:
					continue
				# Otherwise, check if found the goal state.
				elif next == graph.GetGoal():
					# Yield the path followed to obtain the goal.
					yield path.append(next)		
				else:
					path.append(next)
					queue.append((next, path))	

newgame = EightPuzzle([])
bfsearch = BreadthFirst()
list1 = list(bfsearch.bfs())


