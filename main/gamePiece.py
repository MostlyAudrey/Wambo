RED = (202, 52, 51)
GREEN = (67, 124, 23)
GREY = (200, 200, 200)
WHITE = 255
BLACK = 0


class GamePiece:
    num_on_red_bench = 0
    num_on_green_bench = 0

    def __init__(self, piece_color, size, game_size):
        self.node = None
        self.x = None
        self.y = None
        self.color = piece_color
        self.size = size * game_size
        self.game_size = game_size

    def putOnBench(self):
        self.node = None
        self.x = (self.game_size * .95) - (GamePiece.num_on_green_bench * 1.5 * self.size)
        self.y = self.game_size * .95
        if self.color == RED:
            self.y = self.game_size * .05
            self.x = (self.game_size * .05) + (GamePiece.num_on_red_bench * 1.5 * self.size)
            GamePiece.num_on_red_bench += 1
        else:
            GamePiece.num_on_green_bench += 1
        self.drawPiece()

    def drawBorder(self):
        if self.node:
            fill(BLACK)
            ellipse(self.node.x, self.node.y, self.size * 1.1, self.size * 1.1)
        else:
            fill(BLACK)
            ellipse(self.x, self.y, self.size * 1.1, self.size * 1.1)
        self.drawPiece()

    def drawPiece(self):
        if self.node:
            fill(self.color[0], self.color[1], self.color[2])
            ellipse(self.node.x, self.node.y, self.size, self.size)
        else:
            fill(self.color[0], self.color[1], self.color[2])
            ellipse(self.x, self.y, self.size, self.size)

    def undrawBorder(self):
        noStroke()
        if self.node:
            fill(GREY[0], GREY[1], GREY[2])
            ellipse(self.node.x, self.node.y, self.size * 1.15, self.size * 1.15)
            self.node.drawNode()
        else:
            fill(WHITE)
            ellipse(self.x, self.y, self.size * 1.15, self.size * 1.15)
        stroke(BLACK)
        self.drawPiece()

    def undrawPiece(self):
        noStroke()
        if self.node:
            fill(GREY[0], GREY[1], GREY[2])
            ellipse(self.node.x, self.node.y, self.size * 1.1, self.size * 1.1)
        else:
            fill(WHITE)
            ellipse(self.x, self.y, self.size * 1.1, self.size * 1.1)
        stroke(BLACK)

    def setNode(self, node):
        if self.node:
            self.node.occupied = None
        self.undrawPiece()
        if self.x or self.y:
            if self.color == RED:
                GamePiece.num_on_red_bench -= 1
            else:
                GamePiece.num_on_green_bench -= 1
        result = node.setOccupied(self)
        if result:
            self.node = node
            self.x = None
            self.y = None
            return result
        self.putOnBench()
        self.drawPiece()
        return 1

    def checkCollision(self, x, y):
        if self.x:
            if self.x - self.size / 2 < x < self.x + self.size / 2:
                if self.y - self.size / 2 < y < self.y + self.size / 2:
                    return True
            return False
        else:
            return self.node.checkCollision(x, y)

    def __str__(self):
        return str(self.node) + ", colour: " + str(self.color)
