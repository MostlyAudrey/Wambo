from node import Node, GameManager

GAME_MANAGER = ''
GAME_SIZE  = 1000
NODE_WIDTH = .15
RED   = (202,52,51)
GREEN = (67,124,23)
GREY  = (200, 200, 200)
WHITE = 255
BLACK = 0

def setup():
    # This is called on initialization
    background(color(WHITE))
    size( GAME_SIZE, GAME_SIZE )
    GAME_MANAGER = GameManager(GAME_SIZE)
    for i in range( len( GAME_MANAGER.nodes ) ):
        node = GAME_MANAGER.nodes[i]
        if i == 0:
            fill(color(RED[0],RED[1],RED[2]))
        elif i == 23:
            fill(color(GREEN[0],GREEN[1],GREEN[2]))
        else:
            fill(color(GREY[0],GREY[1],GREY[2]))
        ellipse( node.x, node.y, GAME_SIZE * NODE_WIDTH, GAME_SIZE * NODE_WIDTH )
        fill(BLACK)
        ellipse( node.x, node.y, GAME_SIZE * NODE_WIDTH / 10, GAME_SIZE * NODE_WIDTH / 10 )
        for neighbor in node.neighbors:
            line( node.x, node.y, neighbor.x, neighbor.y )

def draw():
    pass
    #This is called every frame
