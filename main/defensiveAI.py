from playerIntelligence import PlayerIntelligence


class DefensiveAI(PlayerIntelligence):

    def picking_piece(self, mouse_click):
        # TODO actually make a decision on what piece to pick
        #  and not just pick the first piece
        piece = self.pieces[0]
        self.selected_piece = piece
        piece.drawBorder()
        return 1

    def show_possible_moves(self, mouse_click):
        if self.possible_moves is None:
            self.possible_moves = PlayerIntelligence.compute_possible_moves(self, self.selected_piece)
            PlayerIntelligence.draw_possible_moves(self, self.possible_moves, self.selected_piece)
            return 0
        else:
            node = self.possible_moves[0]
            self.selected_piece.undrawBorder()
            node.remove_highlight()
            return self.selected_piece.setNode(node)

    def commit_move(self, mouse_click):
        PlayerIntelligence.undraw_possible_moves(self, self.possible_moves)
        self.selected_piece = None
        self.possible_moves = None
        return True
