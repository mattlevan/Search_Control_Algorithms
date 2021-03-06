import random

class SlidingTiles():
    def __init__(self):
        # Seven possible goals of game. 'w' is WHITE, 'b' is BLACK, 0 is BLANK.
        self.goals = [[0,'w','w','w','b','b','b'],
                     ['w',0,'w','w','b','b','b'],
                     ['w','w',0,'w','b','b','b'],
                     ['w','w','w',0,'b','b','b'],
                     ['w','w','w','b',0,'b','b'],
                     ['w','w','w','b','b',0,'b'],
                     ['w','w','w','b','b','b',0]]
        self.goals = set([(0,'w','w','w','b','b','b'),
                     ('w',0,'w','w','b','b','b'),
                     ('w','w',0,'w','b','b','b'),
                     ('w','w','w',0,'b','b','b'),
                     ('w','w','w','b',0,'b','b'),
                     ('w','w','w','b','b',0,'b'),
                     ('w','w','w','b','b','b',0)])


    '''
    Generates a random start state that is NOT a goal state.

    '''
    def gen_start(self):
        start = ['w','w','w',0,'b','b','b']
        random.shuffle(start)

        if set(start) not in self.goals:
            return start
        else:
            self.gen_start()
        self.start = ['w','w','w',0,'b','b','b']
        random.shuffle(self.start)

        if tuple(self.start) not in self.goals:
            return self.start
        else:
            return self.gen_start()


    '''
    Finds all possible moves depending on the position of the blank tile.

    '''
    def find_moves(self, start):
        children = [] # The list of possible moves from the start state.
        moves = [] # Stores the index of each possible move.
        zero_index = start.index(0) # Get index of blank tile.

        # Define legal moves based on the position of the blank space.
        for i in range(1,4):
            right = zero_index+i
            left = zero_index-i

            if right <= 6:
                moves.append(right)
            if left >= 0:
                moves.append(left)

        return moves


    '''
    Generates moves based on the rules of the sliding tiles game.

    '''
    def gen_moves(self, start):
        moves = self.find_moves(start) # Find the moves and store in a list.
        children = []
        move = start

        moves = self.find_moves(list(start)) # Find the moves and store in a list.
        children = []
        move = start
        print('moves ', moves)
        # Find the index of blank space.
        zero_index = start.index(0)

        for i in range(len(moves)): # Generate all children with 0 tile swap.
            # Assign the start state to the current move.
            move = start
            move = list(start)
            print(move)
            # Swap the 0 tile with the ith tile.
            move[i], move[zero_index] = move[zero_index], move[i]
            print(move)
            # Append each move state to the children list.
            children.append(move)
            children.append(tuple(move))

        # Return start as a tuple so it may be used as a key in a dict and
        # return the list of children states generated by this method.
        return tuple(start), children


    '''
    Getter method that returns the goal states of the eight puzzle game.

    '''
    def get_goals(self):
        return self.goals

st = SlidingTiles()
print(st.gen_moves(st.gen_start()))
