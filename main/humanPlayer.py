from playerIntellegence import PlayerIntellegence

RED   = (202,52,51)
GREEN = (67,124,23)
GREY  = (200, 200, 200)
BLUE  = (0, 128, 255)
WHITE = 255
BLACK = (0, 0, 0)
NUM_MOVES = 2
RED_START_NODES = [3,4]
GREEN_START_NODES = [19,20]

class HumanPlayer(PlayerIntellegence):
    
    def picking_piece(self, mouse_click):
        if not mouse_click:
            return 0
        else:
            for piece in self.pieces:
                if piece.checkCollision(mouse_click.x, mouse_click.y):
                    self.selected_piece = piece
                    piece.drawBorder()
                    return 1
       
    def show_possible_moves(self, mouse_click):
        if self.possible_moves == None:
            node_stack = []
            nodes_to_color = []
            if self.selected_piece.node:
                node_stack.append( (self.selected_piece.node, 0) )
            else:
                start_indexes = GREEN_START_NODES
                if self.player_color == RED:
                    start_indexes = RED_START_NODES
                for index in start_indexes:
                    node_stack.append( (self.node_list[index], 1) )
            while len(node_stack):
                curr = node_stack.pop()
                if curr[0].occupied:
                    if curr[0].occupied.color != self.player_color:
                        nodes_to_color.append(curr[0])
                        continue
                else:
                    nodes_to_color.append(curr[0])
                if curr[1] < NUM_MOVES:
                    for child in curr[0].neighbors:
                        node_stack.append((child, curr[1] + 1))
            nodes_to_color = list(dict.fromkeys(nodes_to_color))
            self.possible_moves = nodes_to_color
            self._draw_possible_moves()
            return 0
        if not mouse_click:
            return 0
        if self.selected_piece.checkCollision(mouse_click.x, mouse_click.y):
            self.selected_piece.undrawBorder()
            self.selected_piece = None
            self._undraw_possible_moves()
            self.possible_moves = None
            return 2
        for node in self.possible_moves:
            if node.checkCollision(mouse_click.x, mouse_click.y):
                self.selected_piece.undrawBorder()
                node.remove_highlight()
                return self.selected_piece.setNode( node )

    def _draw_possible_moves(self):
        for node in self.possible_moves:
            if node.occupied:
                if node.occupied.color == self.player_color:
                    self.possible_moves.remove(node)
                    continue
                if ( node.label in RED_START_NODES or node.label in GREEN_START_NODES ) and not self.selected_piece.node:
                    self.possible_moves.remove(node)
                    continue
                node.highlight(BLUE)
            else:
                node.highlight(BLACK)
    
    def _undraw_possible_moves(self):
        for piece in self.possible_moves:
            piece.remove_highlight()
        
    def commit_move(self, mouse_click):
        self._undraw_possible_moves()
        self.selected_piece = None
        self.possible_moves = None
        return True
