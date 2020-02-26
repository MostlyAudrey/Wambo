from node import Node, GameManager, Player, GamePiece
from playerIntellegence import PlayerIntellegence
from humanPlayer import HumanPlayer 
from aggressiveAI import AggressiveAI
from defensiveAI import DefensiveAI

# Constants
# Game States
PICK_PIECE          = 0
SHOW_POSSIBLE_MOVES = 1
MOVE_MADE           = 2

# Game Sizes
GAME_SIZE             = 1000
NODE_PERCENT          = .15
CENTER_PERCENT        = .1
PIECE_PERCENT         = .5
NUM_PIECES_PER_PLAYER = 3

# Determine the types of players
PLAYER_ONE_INT        = HumanPlayer()
PLAYER_TWO_INT        = HumanPlayer()

# Game Manager
GAME_MANAGER = GameManager(GAME_SIZE, PICK_PIECE, NODE_PERCENT, CENTER_PERCENT, NUM_PIECES_PER_PLAYER, PIECE_PERCENT, PLAYER_ONE_INT, PLAYER_TWO_INT)

# Colors
RED   = ( 202, 52,  51  )
GREEN = ( 67,  124, 23  )
GREY  = ( 200, 200, 200 )
BLACK = ( 0,   0,   0   )
WHITE = 255

# Global Variables
turn_counter = 0
active_player = 0

def setup():
    # This is called on initialization
    background(color(WHITE))
    size( GAME_SIZE, GAME_SIZE )
    for i in range( len( GAME_MANAGER.nodes ) ):
        node = GAME_MANAGER.nodes[i]
        if i == 0:
            node._draw(RED, BLACK)
        elif i == 23:
            node._draw(GREEN, BLACK)
        else:
            node._draw(GREY, BLACK)
            
def draw():
    # This function is called every frame
    player_logic = GAME_MANAGER.players[active_player].intellegence
    # Switcher acts as a basic Finite State Machine
    switcher = {
        PICK_PIECE          : player_logic.picking_piece,
        SHOW_POSSIBLE_MOVES : player_logic.show_possible_moves,
        MOVE_MADE           : player_logic.commit_move
    }
    # Calls the function associated with the current state
    switcher.get(GAME_MANAGER.game_state, lambda: "Invalid Game State")()
    pass

def _next_turn():
    turn_counter = turn+counter + 1
    active_player = active_player + 1 % 2
    
