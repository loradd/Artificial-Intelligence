__author__ = 'Twitch'
import GameModels as G
import MiniMaxOthello as M

def get_players(): # ritorna le strategie dei giocatori
    black = M.minimax_searcher(2, M.weight_score) # altezza e metodo di valutazione
    white = M.minimax_searcher(3, M.weight_score)
    return black, white

# MAIN
black, white = get_players()
board, score = G.play(black, white)
print 'Final score:', score
print '%s wins!' % ('Black' if score > 0 else 'White')
