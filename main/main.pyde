from gameManager import GameManager
from node import Node, MouseAction
from playerIntelligence import PlayerIntelligence
from humanPlayer import HumanPlayer
from aggressiveAI import AgressiveAI
from defensiveAI import DefensiveAI

# Constants
# Game States
PICK_PIECE          = 0
SHOW_POSSIBLE_MOVES = 1
MOVE_MADE           = 2
GAME_OVER           = 3

# Game Sizes
GAME_SIZE             = 800
NODE_PERCENT          = .1
CENTER_PERCENT        = .1
PIECE_PERCENT         = .5
NUM_PIECES_PER_PLAYER = 3

# Determine the types of players
PLAYER_ONE_INT        = "HumanPlayer"
PLAYER_TWO_INT        = "HumanPlayer"

# Game Manager
GAME_MANAGER = None
# Colors
RED   = ( 202, 52,  51  )
GREEN = ( 67,  124, 23  )
GREY  = ( 200, 200, 200 )
BLACK = ( 0,   0,   0   )
WHITE = 255

# Global Variables
turn_counter = 0
active_player = 0
last_mouse_click = None


def setup():
    # This is called on initialization
    background(color(WHITE))
    size( GAME_SIZE, GAME_SIZE)
    global GAME_MANAGER
    GAME_MANAGER = GameManager(GAME_SIZE, PICK_PIECE, NODE_PERCENT, CENTER_PERCENT, NUM_PIECES_PER_PLAYER, PIECE_PERCENT, PLAYER_ONE_INT, PLAYER_TWO_INT)
    for i in range( len( GAME_MANAGER.nodes ) ):
        node = GAME_MANAGER.nodes[i]
        if i == 0:
            node.drawNode(RED, BLACK)
        elif i == 23:
            node.drawNode(GREEN, BLACK)
        else:
            node.drawNode(GREY, BLACK)
    for player in GAME_MANAGER.players:
        for piece in player.pieces:
            piece.putOnBench()
    _draw_active_player()


def draw():
    # This function is called every frame
    player_logic = GAME_MANAGER.players[active_player]
    # Switcher acts as a basic Finite State Machine
    switcher = {
        PICK_PIECE          : player_logic.picking_piece,
        SHOW_POSSIBLE_MOVES : player_logic.show_possible_moves,
        MOVE_MADE           : player_logic.commit_move,
        GAME_OVER           : player_logic.game_over
    }
    # Calls the function associated with the current state
    global last_mouse_click
    _next_state( switcher.get(GAME_MANAGER.game_state, lambda: "Invalid Game State")(last_mouse_click) )
    last_mouse_click = None
    pass


def mouseClicked():
    global last_mouse_click
    last_mouse_click = MouseAction(mouseX, mouseY)


def _next_state(command):
    global turn_counter
    global active_player
    global GAME_MANAGER

    if command == 1:
        if GAME_MANAGER.game_state == PICK_PIECE:
            GAME_MANAGER.game_state = SHOW_POSSIBLE_MOVES
            return
        if GAME_MANAGER.game_state == SHOW_POSSIBLE_MOVES:
            GAME_MANAGER.game_state = MOVE_MADE
            return
        if GAME_MANAGER.game_state == MOVE_MADE:
            turn_counter = turn_counter + 1
            active_player = ( active_player + 1 ) % 2
            _draw_active_player()
            GAME_MANAGER.game_state = PICK_PIECE
            return
    if command == 2:
        if GAME_MANAGER.game_state == SHOW_POSSIBLE_MOVES:
            GAME_MANAGER.game_state = PICK_PIECE
            return
        if GAME_MANAGER.game_state == SHOW_POSSIBLE_MOVES:
            GAME_MANAGER.game_state = PICK_PIECE
            return
    if command == 3:
        GAME_MANAGER.game_state = GAME_OVER
        color = GAME_MANAGER.players[active_player].player_color
        background( color[0], color[1], color[2] )
    if command == 4:
        setup()


def _draw_active_player():
    color = GAME_MANAGER.players[active_player].player_color
    fill( color[0], color[1], color[2] )
    ellipse( GAME_SIZE / 2, GAME_SIZE / 2, GAME_SIZE * NODE_PERCENT, GAME_SIZE * NODE_PERCENT )
