import Game
import random

class MissionaryCannibal(Game):
    def __init__(self, start):
        # Goal states are ones where Ms and Cs cross without any conversions.

        # Start state needs shuffling.
        self.start = ['w','w','w',0,'b','b','b']


    '''
    Generates a random start state that is NOT a goal state.

    '''
    def gen_start(self):
        start = ['w','w','w',0,'b','b','b']

        if start not in self.goals:
            return start
        else:
            random.shuffle(start)
            gen_start(start,goals)


    '''
    Finds all possible moves depending on the position of the blank tile.

    '''
    def find_moves(self, start):
        children = [] # The list of possible moves from the start state.
        zero_index = 0 # Zero index stores index of the blank tile (0) position.
        moves_index = [] # Stores the index of each possible move.

        # Find the index of blank space.
        for i in range(len(start)):
            if start[i] == 0:
                zero_index = i

        # Define legal moves based on the position of the blank space.
        swaps = [] # List of indices which may be swapped with blank.
        for i in range(1,4):
            right = zero_index+i
            left = zero_index-i

            if right <= 6:
                swaps.append(right)

            if left >= 0:
                swaps.append(left)

        moves_index.extend((swaps)) # Add all elements of swaps to moves_index.

        return moves_index

    '''
    Generates moves based on the rules of the eight puzzle game.

    '''
    def gen_moves(self, start):
        moves_index = find_moves(start) # Find the moves and store in a list.

        for i in moves_index: # Generate all children with 0 tile swap.
            # Assign the start state to the current move.
            move = start

            # Swap the 0 tile with the ith possible tile.
            move[i], move[zero_index] = move[zero_index], move[i]

            # Append each move state to the children list.
            children.append(move)

        # Return start as a tuple so it may be used as a key in a dict and
        # return the list of children states generated by this method.
        return tuple(start), children


    '''
    Getter method that returns the goal states of the eight puzzle game.

    '''
    def get_goals(self):
        return self.goals
