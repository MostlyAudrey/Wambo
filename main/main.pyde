from gameManager import GameManager
from node import Node, MouseAction
from playerIntelligence import PlayerIntelligence
from humanPlayer import HumanPlayer
from AI import AI

# Constants
# Game States
INIT_SCREEN         = -1
PICK_PIECE          = 0
SHOW_POSSIBLE_MOVES = 1
MOVE_MADE           = 2
GAME_OVER           = 3
STARTING_STATE = INIT_SCREEN

# Game Sizes
GAME_SIZE             = 800
NODE_PERCENT          = .1
CENTER_PERCENT        = .1
PIECE_PERCENT         = .5
NUM_PIECES_PER_PLAYER = 3

# Determine the types of players
# Param 0: which type of player to select
# Param 1: offensive=True, defensive=False
# Param 2: aggressive=True, passive=False
PLAYER_ONE_INT        = ['AI', 'True', 'True']
PLAYER_TWO_INT        = ['AI', 'False', 'False']

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

#boxes
boxes = []
options_1 = [('AI', True), ('Offensive', True), ('Aggressive', True), ('AI', True), ('Offensive', True), ('Aggressive', True)]
options_2 = [('Human', False), ('Defensive', False), ('Passive', False), ('Human', False), ('Defensive', False), ('Passive', False)]
number_of_trials = 10
results = []


def setup():
    # This is called on initialization
    background(color(WHITE))
    size( GAME_SIZE, GAME_SIZE)
    global GAME_MANAGER
    GAME_MANAGER = GameManager(GAME_SIZE, STARTING_STATE, NODE_PERCENT, CENTER_PERCENT, NUM_PIECES_PER_PLAYER, PIECE_PERCENT, PLAYER_ONE_INT, PLAYER_TWO_INT)
    if GAME_MANAGER.game_state != INIT_SCREEN:
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
    if GAME_MANAGER.game_state == INIT_SCREEN:
        drawMenuScreen(last_mouse_click)
    else:
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
    global number_of_trials
    global results
    global PLAYER_ONE_INT
    global PLAYER_TWO_INT

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
        if number_of_trials == 0:
            writeToFile(PLAYER_ONE_INT, PLAYER_TWO_INT, results)
            print('done')
            GAME_MANAGER.game_state = GAME_OVER
            color = GAME_MANAGER.players[active_player].player_color
            background( color[0], color[1], color[2] )
        else:
            results.append({'winner': 'Player ' + str(active_player + 1), 'turns': turn_counter})
            print(str(number_of_trials) + " trial(s) remaining")
            number_of_trials -= 1
            turn_counter = 0
            active_player = 0
            STARTING_STATE = PICK_PIECE
            setup()
    if command == 4:
        setup()


def _draw_active_player():
    color = GAME_MANAGER.players[active_player].player_color
    fill( color[0], color[1], color[2] )
    ellipse( GAME_SIZE / 2, GAME_SIZE / 2, GAME_SIZE * NODE_PERCENT, GAME_SIZE * NODE_PERCENT )
    
def writeToFile(player_1_info, player_two_info, results):
    player_1_offensive = 'Offensive' if player_1_info[1] == 'True' else 'Defensive'
    player_1_agressive = 'Aggressive' if player_1_info[2] == 'True' else 'Passive'
    player_2_offensive = 'Offensive' if player_two_info[1] == 'True' else 'Defensive'
    player_2_agressive = 'Agressive' if player_two_info[2] == 'True' else 'Defensive'
    turns = []
    filename = player_1_offensive + '-' + player_1_agressive + ' vs. ' + player_2_offensive + '-' + player_2_agressive + ' ' + str(len(results)) + ' Trials'
    f1=open('../' + filename + '.txt', 'w+')
    f1.write('Player 1 is ' + player_1_offensive + '/' + player_1_agressive + '. Player 2 is ' + player_2_offensive + '/' + player_2_agressive + '\n')
    player_1_wins = 0
    player_2_wins = 0
    for dictionary in results:
        f1.write(dictionary['winner'] + ' won in ' + str(dictionary['turns']) + ' turns\n')
        turns.append(dictionary['turns'])
        if dictionary['winner'] == 'Player 1':
            player_1_wins += 1
        else:
            player_2_wins += 1
    f1.write('Player 1: ' + str(player_1_wins) + ' wins. Player 2: ' + str(player_2_wins) + ' wins\n')
    average = sum(turns) / len(turns)
    std = standard_deviation(turns, average)
    f1.write('Average Turns: ' + str(average) + '\n')
    f1.write('Standard Deviation of Turns ' + str(std) + '\n')
    f1.close()
        
def standard_deviation(turns, average):
    sum = 0
    for turn in turns:
        difference = (turn - average) ** 2
        sum += difference
    sum /= len(turns)
    return sum ** 0.5
    
def drawMenuScreen(mouse_click):
    #6 boxes of width 60
    global STARTING_STATE
    global number_of_trials
    box_size = 100
    total_width = 6 * box_size
    start = (GAME_SIZE - total_width) / 2
    y_pos = GAME_SIZE / 2
    background(color(WHITE))
    stroke (0)
    
    fill(22)
    text('Press Enter To Begin', GAME_SIZE / 2 - 70, 50)
    
    fill(22)
    text('Number of Trials: ' + str(number_of_trials) + '. Press up and down keys to adjust', GAME_SIZE / 2 - 170, 100)
    
    #draw player 1 box
    fill(222)
    rect(start, y_pos, box_size * 3, box_size)
    fill(22)
    text('Player 1 Options (Green means selected)', start + 10, y_pos + 20)
    
    #draw player 2 box
    fill(222)
    new_start = start + box_size * 3
    rect(new_start, y_pos, box_size * 3, box_size)
    fill(22)
    text('Player 2 Options (Green means selected)', new_start + 10, y_pos + 20)
    
    y_pos += box_size
    
    for i in range(start, start + total_width, box_size): 
        text_index = int((i - start) / box_size)
        fill(0, 255, 0) if options_1[text_index][1] else fill(255,0, 0)
        rect(i, y_pos, box_size, box_size / 2)
        fill(22)
        text(options_1[text_index][0], i + 10, y_pos + 20)
        boxes.append((i, i + box_size, y_pos, y_pos + box_size / 2))
        
        fill(0, 255, 0) if options_2[text_index][1] else fill(255,0, 0)
        rect(i, y_pos + box_size / 2, box_size, box_size / 2)
        fill(22)
        text(options_2[text_index][0], i + 10, y_pos + box_size / 2 + 20)
        boxes.append((i, i + box_size, y_pos, y_pos + box_size))
        
    if mouse_click:
        x = mouse_click.x
        y = mouse_click.y
        
        for index, option_box in enumerate(boxes):
            x1, x2, y1, y2 = option_box
            if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                i = int(index / 2)
                options_1[i] = (options_1[i][0], not options_1[i][1])
                options_2[i] = (options_2[i][0], not options_2[i][1])
                break;
    
    if keyPressed:
        if keyCode == UP or keyCode == RIGHT:
            number_of_trials += 1
        elif keyCode == DOWN or keyCode == LEFT:
            number_of_trials -= 1
        elif key == ENTER or key == RETURN:
            global PLAYER_ONE_INT
            global PLAYER_TWO_INT
            PLAYER_ONE_INT = []
            PLAYER_TWO_INT = []
            for index, option in enumerate(options_1):
                if index == 0:
                    PLAYER_ONE_INT.append('AI' if option[1] else 'HUMAN')
                elif index == 3:
                    PLAYER_TWO_INT.append('AI' if option[1] else 'HUMAN')
                elif index < 3:
                    PLAYER_ONE_INT.append('True' if option[1] else 'False')
                else:
                    PLAYER_TWO_INT.append('True' if option[1] else 'False')
            STARTING_STATE = PICK_PIECE
            setup()
            
            
