from random import random
RED   = (202,52,51)
GREEN = (67,124,23)
GREY  = (200, 200, 200)
WHITE = 255
BLACK = 0
PERCENT_ATTACKER_WINS = 0.5

class Node:
    def __init__(self, node_size, center_size, label):
        self.neighbors = []
        self.x = 0
        self.y = 0
        self.node_size = node_size
        self.center_size = center_size
        self.label = label
        self.occupied = None
        
    def set(self, list, x, y, goal = None):
        self.neighbors = list
        self.x = x
        self.y = y
        self.goal = goal
        
    def drawNode(self, node_color = None, center_color = None):
        if node_color:
            self.node_color = node_color
        if center_color:
            self.center_color = center_color
        fill( self.node_color[0], self.node_color[1], self.node_color[2])
        ellipse( self.x, self.y, self.node_size, self.node_size )
        fill( self.center_color[0], self.center_color[1], self.center_color[2])
        ellipse( self.x, self.y, self.center_size, self.center_size )
        for neighbor in self.neighbors:
            line( self.x, self.y, neighbor.x, neighbor.y )
        if self.occupied:
            self.occupied.drawPiece()

    def checkCollision(self, x, y):
        if x > self.x - self.node_size / 2 and x < self.x + self.node_size / 2:
                if y > self.y - self.node_size / 2 and y < self.y + self.node_size / 2:
                    return True
        return False

    def highlight(self, fill_color):
        fill(fill_color[0], fill_color[1], fill_color[2])
        ellipse( self.x, self.y, self.node_size*1.1, self.node_size*1.1 )
        self.drawNode()
        
    def remove_highlight(self):
        noStroke()
        fill(WHITE)
        ellipse( self.x, self.y, self.node_size*1.15, self.node_size*1.15 )
        stroke(BLACK)
        self.drawNode()
    
    def setOccupied(self, piece):
        if self.occupied:
            if random() < PERCENT_ATTACKER_WINS:
                return 0
            else:
                self.occupied.putOnBench()
        self.occupied = piece
        if self.goal and piece.color == self.goal:
            return 3
        return 1
        
    def __str__(self):
        return "node: " + str(self.label)

class MouseAction:
    def __init__(self, x, y):
        self.x = x
        self.y = y
