RED   = (202,52,51)
GREEN = (67,124,23)
GREY  = (200, 200, 200)
WHITE = 255
BLACK = (0, 0, 0)

class Node:
    def __init__(self, node_size, center_size):
        self.neighbors = []
        self.x = 0
        self.y = 0
        self.node_size = node_size
        self.center_size = center_size
    def set(self, list, x, y):
        self.neighbors = list
        self.x = x
        self.y = y
    def _draw(self, node_color, center_color):
        fill(node_color[0],node_color[1],node_color[2])
        ellipse( self.x, self.y, self.node_size, self.node_size )
        fill(center_color[0],center_color[1],center_color[2])
        ellipse( self.x, self.y, self.center_size, self.center_size )
        for neighbor in self.neighbors:
            line( self.x, self.y, neighbor.x, neighbor.y )

class GameManager:
    def __init__(self, game_size, game_state, node_percent, center_percent, pieces_per_player, piece_size_percent):
        self.selected_piece =''
        self.game_state = game_state
        self.players = [ 
            Player(RED, pieces_per_player, game_size * node_percent * piece_size_percent),
            Player(GREEN, pieces_per_player, game_size * node_percent * piece_size_percent)
        ]
        self.nodes = []
        for i in range(24):
            self.nodes.append(Node(game_size * node_percent, game_size * node_percent * center_percent))
        
        s1 = game_size * .1
        s2 = game_size * .3
        s3 = game_size * .5
        s4 = game_size * .7
        s5 = game_size * .9

        self.nodes[0].set( [self.nodes[1], self.nodes[2]], s3, s1 )
        self.nodes[1].set( [self.nodes[0], self.nodes[3]], s2, s1 )
        self.nodes[2].set( [self.nodes[0], self.nodes[4]], s4, s1 )
        self.nodes[3].set( [self.nodes[1], self.nodes[7], self.nodes[9]], s1, s1 ) 
        self.nodes[4].set( [self.nodes[2], self.nodes[6], self.nodes[8]], s5, s1 )
        self.nodes[5].set( [self.nodes[6], self.nodes[7]], s3, s2 )
        self.nodes[6].set( [self.nodes[4], self.nodes[5], self.nodes[10]], s4, s2 )
        self.nodes[7].set( [self.nodes[3], self.nodes[5], self.nodes[11]], s2, s2 )
        self.nodes[8].set( [self.nodes[4], self.nodes[12]], s5, s2 ) 
        self.nodes[9].set( [self.nodes[3], self.nodes[13]], s1, s2 )
        self.nodes[10].set( [self.nodes[6], self.nodes[12], self.nodes[14]], s4, s3 )
        self.nodes[11].set( [self.nodes[7], self.nodes[13], self.nodes[15]], s2, s3 )
        self.nodes[12].set( [self.nodes[8], self.nodes[10], self.nodes[16]], s5, s3 )
        self.nodes[13].set( [self.nodes[9], self.nodes[11], self.nodes[17]], s1, s3 )
        self.nodes[14].set( [self.nodes[10], self.nodes[18], self.nodes[20]], s4, s4 )
        self.nodes[15].set( [self.nodes[11], self.nodes[18], self.nodes[19]], s2, s4 )
        self.nodes[16].set( [self.nodes[12], self.nodes[20]], s5, s4 )
        self.nodes[17].set( [self.nodes[13], self.nodes[19]], s1, s4 ) 
        self.nodes[18].set( [self.nodes[14], self.nodes[15]], s3, s4 )
        self.nodes[19].set( [self.nodes[15], self.nodes[17], self.nodes[21]], s1, s5 )
        self.nodes[20].set( [self.nodes[14], self.nodes[16], self.nodes[22]], s5, s5 )
        self.nodes[21].set( [self.nodes[19], self.nodes[23]], s2, s5 )
        self.nodes[22].set( [self.nodes[20], self.nodes[23]], s4, s5 ) 
        self.nodes[23].set( [self.nodes[21], self.nodes[22]], s3, s5 )

class Player:
    # inputs:
    #     player_color is the player color
    #     num_pieces is the number of pieces the player has
    #     piece_size of a players game piece
    def __init__(self, player_color, num_pieces, piece_size ):
        self.pieces = []
        for i in range( num_pieces ):
            self.pieces.append( GamePiece( player_color, piece_size ) )

class GamePiece:
    def __init__(self, piece_color, size):
        self.node = ''
        self.color = piece_color
        self.size = size

    def drawPiece(self):
        if self.node != '':
            fill( self.color[0], self.color[1], self.color[2] )
            ellipse( node.x, node.y, self.size, self.size)
