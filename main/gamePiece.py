RED   = (202,52,51)
GREEN = (67,124,23)
GREY  = (200, 200, 200)
WHITE = 255
BLACK = (0, 0, 0)

class GamePiece:
    num_on_red_bench = 0
    num_on_green_bench = 0
    
    def __init__(self, piece_color, size, game_size):
        self.node  = None
        self.x     = 0
        self.y     = 0
        self.color = piece_color
        self.size  = size * game_size
        self.game_size = game_size
    
    def putOnBench(self):
        self.x = ( self.game_size * .95 ) - ( GamePiece.num_on_green_bench * 1.5 * self.size )
        self.y = self.game_size * .95
        if self.color == RED:
            self.y = self.game_size * .05
            self.x = ( self.game_size * .05 ) + ( GamePiece.num_on_red_bench * 1.5 * self.size )
            GamePiece.num_on_red_bench = GamePiece.num_on_red_bench + 1
        else: GamePiece.num_on_green_bench = GamePiece.num_on_green_bench + 1
        self.drawPiece()

    def drawPiece(self):
        if self.node:
            fill( self.color[0], self.color[1], self.color[2] )
            ellipse( node.x, node.y, self.size, self.size)
        else:
            fill( self.color[0], self.color[1], self.color[2] )
            ellipse( self.x, self.y, self.size, self.size)
    
    def checkCollision(self, x, y):
        if self.x:
            if x > self.x - self.size / 2 and x < self.x + self.size / 2:
                if y > self.y - self.size / 2 and y < self.y + self.size / 2:
                    return True
            return False
        else:
            return self.node.checkCollision(x,y)
            
