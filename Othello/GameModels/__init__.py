__author__ = 'Twitch'

EMPTY = '.'
BLACK = 'B'
WHITE = 'W'
BORDER = 'X'

CELLS = (EMPTY, BLACK, WHITE, BORDER)
PLAYERS = {BLACK: 'Black', WHITE: 'White'}

UP = -10
DOWN = 10
LEFT = -1
RIGHT = 1
UP_RIGHT = -9
UP_LEFT = -11
DOWN_RIGHT = 11
DOWN_LEFT = 9

DIRECTIONS = (UP, DOWN, LEFT, RIGHT, UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)


# celle interne tavola
def available_cells():
    return [cells for cells in xrange(11, 89) if 1 <= (cells % 10) <= 8]


# inizializza tavola
def init_board():
    board = [BORDER] * 100
    for cell in available_cells():
        board[cell] = EMPTY

    board[44] = WHITE
    board[55] = WHITE
    board[45] = BLACK
    board[54] = BLACK
    return board


#stampa tavola
def print_board(board):
    rep = ''
    rep += '  %s\n' % ' '.join(map(str, range(1, 9)))
    for row in xrange(1, 9):
        start_row = 10*row + 1
        end_row = 10*row + 9
        rep += '%d %s\n' % (row, ' '.join(board[start_row:end_row]))
    return rep


# mossa valida
def valid_move(move):
    return isinstance(move, int) and move in available_cells()


# colore avversario
def opponent_color(player):
    return BLACK if player is WHITE else WHITE


# trova posizione per creare ponte su pedine avversarie
def find_bridge(square, player, board, direction):
    bridge = square + direction
    if board[bridge] == player:
        return None
    opp = opponent_color(player)
    while board[bridge] == opp:
        bridge += direction
    return None if board[bridge] in (BORDER, EMPTY) else bridge


# mossa legale
def legal_move(move, player, board):
    hasbridge = lambda direction: find_bridge(move, player, board, direction)
    return board[move] == EMPTY and any(map(hasbridge, DIRECTIONS))


# gestione eccezione mossa illegale ( vedi get_move )
class IllegalMoveError(Exception):
    def __init__(self, player, move, board):
        self.player = player
        self.move = move
        self.board = board

    def __str__(self):
        return '%s move to square %d is not legal' % (PLAYERS[self.player], self.move)


# applica mossa su tavola
def make_move(move, player, board):
    board[move] = player
    for direction in DIRECTIONS:
        make_changes(move, player, board, direction)
    print print_board(board)
    return board


# mangia pedine avversarie dopo mossa
def make_changes(move, player, board, direction):
    bridge = find_bridge(move, player, board, direction)
    if not bridge:
        return
    cell = move + direction
    while cell != bridge:
        board[cell] = player
        cell += direction



# lista mosse legali
def legal_moves_list(player, board):
    return [cell for cell in available_cells() if legal_move(cell, player, board)]


# esistenza almeno una mossa legale
def any_legal_moves(player, board):
    return any(legal_move(cell, player, board) for cell in available_cells())


# gioco othello
def play(black_strategy, white_strategy):
    board = init_board()
    player = BLACK
    strategy = lambda color: black_strategy if color == BLACK else white_strategy
    while player is not None:
        move = get_move(strategy(player), player, board)
        make_move(move, player, board)
        player = next_player(board, player)
        print_board(board)
    return board, score(BLACK, board)

# giocatore turno successivo
def next_player(board, prev_player):
    opp = opponent_color(prev_player)
    if any_legal_moves(opp, board):
        return opp
    elif any_legal_moves(prev_player, board):
        return prev_player
    return None # no legal moves


# mossa in base alla strategia
def get_move(strategy, player, board):
    copy = list(board) # copy the board to prevent cheating
    move = strategy(player, copy)
    if not valid_move(move) or not legal_move(move, player, board):
        raise IllegalMoveError(player, move, copy)
    return move

# valutazione semplice ( differenza numero pedine ) VEDI MINIMAXOTHELLO PER PESATA
def score(player, board):
    player_cells, opponent_cells = 0, 0
    opponent = opponent_color(player)
    for cells in available_cells():
        piece = board[cells]
        if piece == player: player_cells += 1
        elif piece == opponent: opponent_cells += 1
    return player_cells - opponent_cells


