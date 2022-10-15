"""
Tic Tac Toe Player
"""

import math
import copy
import sys
sys.setrecursionlimit(100000)


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_cnt = 0
    O_cnt = 0

    for row in board:
        X_cnt = X_cnt + row.count(X)
        O_cnt = O_cnt + row.count(O)
    
    if X_cnt <= O_cnt:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_cells = set()

    for i in range(len(board)):
        for j in range(3):
            if board[i][j] == EMPTY:
                empty_cells.add((i, j))
    
    return empty_cells


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    board_updated = copy.deepcopy(board)

    board_updated[action[0]][action[1]] = player(board)

    return board_updated

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == X:
                return X
            elif board[0][i] == O:
                return O

    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == O:
                return O
            elif board[i][0] == X:
                return X

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == O:
            return O
        elif board[0][0] == X:
            return X
    elif board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == O:
            return O
        elif board[0][2] == X:
            return X
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # raise NotImplementedError
    if winner(board) == O:
        return True
    elif winner(board) == X:
        return True
    else:
        count = 0
        for each_arr in board:
            count += each_arr.count(X)
            count += each_arr.count(O)
        if count == 9:
            return True
        else:
            return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def min(board):
    if terminal(board):
        return utility(board)

    min_value = math.inf
    for action in actions(board):
        value = max(result(board, action))
        if value < min_value:
            min_value = value
    return min_value


def max(board):
    if terminal(board):
        return utility(board)

    max_value = -math.inf
    for action in actions(board):
        value = min(result(board, action))
        if value > max_value:
            max_value = value
    return max_value

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    optimalAction = None

    if terminal(board):
        return None
    
    if player(board) == X:
        minValue = -math.inf

        for action in actions(board):
            actValue = min(result(board, action))
            if actValue > minValue:
                minValue = actValue
                optimalAction = action

    elif player(board) == O:
        maxValue = math.inf

        for action in actions(board):
            actValue = max(result(board, action))
            if actValue < maxValue:
                maxValue = actValue
                optimalAction = action
                
    return optimalAction
