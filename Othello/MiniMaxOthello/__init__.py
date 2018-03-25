__author__ = 'Twitch'

import GameModels as G

# PESI DELLE CELLE
CELLS_WEIGHTS = [
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0, 120, -20,  20,   5,   5,  20, -20, 120,   0,
    0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0,
    0,  20,  -5,  15,   3,   3,  15,  -5,  20,   0,
    0,   5,  -5,   3,   3,   3,   3,  -5,   5,   0,
    0,   5,  -5,   3,   3,   3,   3,  -5,   5,   0,
    0,  20,  -5,  15,   3,   3,  15,  -5,  20,   0,
    0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0,
    0, 120, -20,  20,   5,   5,  20, -20, 120,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
]

# valutazione pesata
def weight_score(player, board):
    enemy = G.opponent_color(player)
    total = 0
    for cell in G.available_cells():
        if board[cell] == player:
            total += CELLS_WEIGHTS[cell]
        elif board[cell] == enemy:
            total -= CELLS_WEIGHTS[cell]
    return total


def minimax(player, board, depth, evaluate):

    def value(board):
        return -minimax(G.opponent_color(player), board, depth-1, evaluate)[0]

    if depth == 0:
        return evaluate(player, board), None

    moves = G.legal_moves_list(player, board)


    if not moves:
        if not G.any_legal_moves(G.opponent_color(player), board):
            return final_value(player, board), None
        return value(board), None

    return max((value(G.make_move(m, player, list(board))), m) for m in moves)

MAX_VALUE = sum(map(abs, CELLS_WEIGHTS))
MIN_VALUE = -MAX_VALUE

def final_value(player, board):
    diff = G.score(player, board)
    if diff < 0:
        return MIN_VALUE
    elif diff > 0:
        return MAX_VALUE
    return diff

def minimax_searcher(depth, evaluate):
    def strategy(player, board):
        return minimax(player, board, depth, evaluate)[1]
    return strategy
