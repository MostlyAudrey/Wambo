from playerIntelligence import PlayerIntelligence

RED = (202, 52, 51)
GREEN = (67, 124, 23)
GREY = (200, 200, 200)
BLUE = (0, 128, 255)
WHITE = 255
BLACK = (0, 0, 0)
NUM_MOVES = 2
RED_START_NODES = [3, 4]
GREEN_START_NODES = [19, 20]


class HumanPlayer(PlayerIntelligence):

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
        if self.possible_moves is None:
            self.possible_moves = PlayerIntelligence.compute_possible_moves(self, self.selected_piece)
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
                return self.selected_piece.setNode(node)

    def _draw_possible_moves(self):
        for node in self.possible_moves:
            if node.occupied:
                if node.occupied.color == self.player_color:
                    self.possible_moves.remove(node)
                    continue
                if (node.label in RED_START_NODES or node.label in GREEN_START_NODES) and not self.selected_piece.node:
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
