from playerIntelligence import PlayerIntelligence
from gamePiece import GamePiece
import random

RED = (202, 52, 51)
GREEN = (67, 124, 23)

class DefensiveAI(PlayerIntelligence):
    # This counter is used to slow the AI down, so we can see how it is making its move
    # TODO - I'm not sure if this is the best way to do this, so if there is one, please fix this
    wait = 0
    threshold = 100

    def picking_piece(self, mouse_click):
        # Prioritise getting all the pieces out onto the board
        if self.player_color == RED:
            cond = GamePiece.num_on_red_bench != 0
        else:
            cond = GamePiece.num_on_green_bench != 0

        if cond:
            for piece in self.pieces:
                if piece.node is None:
                    self.selected_piece = piece
                    break

            if self.selected_piece is None:
                print "Here, but shouldn't be..."
                print GamePiece.num_on_red_bench
                print GamePiece.num_on_green_bench

                for piece in self.pieces:
                    print piece
        else:
            # Pick one of the pieces, randomly
            pos = random.randint(0, len(self.pieces) - 1)
            self.selected_piece = self.pieces[pos]

        # Highlight the selected piece
        self.selected_piece.drawBorder()
        return 1

    def show_possible_moves(self, mouse_click):
        self.wait += 1

        if self.possible_moves is None:
            self.possible_moves = PlayerIntelligence.compute_possible_moves(self, self.selected_piece)
            PlayerIntelligence.draw_possible_moves(self, self.possible_moves, self.selected_piece)
            return 0
        else:
            if self.wait < self.threshold:
                return 0
            else:
                self.wait = 0

            node = self.possible_moves[0]
            self.selected_piece.undrawBorder()
            node.remove_highlight()
            return self.selected_piece.setNode(node)

    def commit_move(self, mouse_click):
        PlayerIntelligence.undraw_possible_moves(self, self.possible_moves)
        self.selected_piece = None
        self.possible_moves = None
        return True
