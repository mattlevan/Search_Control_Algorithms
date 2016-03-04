'''
BreadthFirst search is a program that finds optimal solutions to games
(using the Game class) by iterating through all possible moves and
comparing to both the game goal state and all previous states visited.

'''
import Eightgame

game = Eightgame()
print('Start of game: ', game.get_start())
print('Goal of game: ', game.get_goal())

start = game.get_start()
goal = game.get_goal()
graph = {}
begin, children = game.Move(start)
update, newchild = game.Move(children[1])
print('Move x: ', update)
print('begin, children', begin, children)
print('update, newchild', update, newchild)
graph.update({begin: children})
graph.update({update: newchild})
print('next move: ', graph)

class BreadthFirst:
    def bfs_paths(game):
        # Ensure correct input.
        if type(game) is not Game:
            print('Breadth first search requires a Game as input.')
            exit(1)

        graph = {}
        currentpath = set()
        start = game.get_start()
        goal = game.get_goal()
        graph.update({goal: 'GOAL'})
        queue = [(tuple(start), [start])]

        while queue:
        # Store the first move in vertex, path
        (vertex,currentpath) = queue.pop()
        # Add the vertex and path to the dictionary graph.
        if vertex not in graph:
            movestart, newstates = game.Move(vertex)
            graph.update({movestart: newstates})
        for next in graph[vertex]:
            if next in currentpath:
                continue

            # Test if the path is the goal state.
            if next == graph[goal]:
                print('Goal state found!')
                return currentpath
            else:
                currentpath.append([next])
                queue.append((next, currentpath))
        # Append the paths to the current path
        # Pop a path from the beginning of nyv.
        # Test if the path is present in graph.
        # Test if the path is the goal state.
        # If the path is not present, then perform a move
x = BreadthFirst
y = x.bfs_paths(game)
