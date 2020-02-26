class Node:
    def __init__(self):
        self.neighbors = []
        self.x = 0
        self.y = 0
    def set(self, list, x, y):
        self.neighbors = list
        self.x = x
        self.y = y

class GameManager:
    def __init__(self, game_size):
        s1 = game_size * .1
        s2 = game_size * .3
        s3 = game_size * .5
        s4 = game_size * .7
        s5 = game_size * .9
        self.nodes = []
        for i in range(24):
            self.nodes.append(Node())
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
