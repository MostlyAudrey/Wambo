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
            PlayerIntelligence.draw_possible_moves(self, self.possible_moves, self.selected_piece)
            return 0
        if not mouse_click:
            return 0
        if self.selected_piece.checkCollision(mouse_click.x, mouse_click.y):
            self.selected_piece.undrawBorder()
            self.selected_piece = None
            PlayerIntelligence.undraw_possible_moves(self, self.possible_moves)
            self.possible_moves = None
            return 2
        for node in self.possible_moves:
            if node.checkCollision(mouse_click.x, mouse_click.y):
                self.selected_piece.undrawBorder()
                node.remove_highlight()
                return self.selected_piece.setNode(node)

    def commit_move(self, mouse_click):
        PlayerIntelligence.undraw_possible_moves(self, self.possible_moves)
        self.selected_piece = None
        self.possible_moves = None
        return True
