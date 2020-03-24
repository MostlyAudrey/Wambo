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
        print("Here2")

    def commit_move(self, mouse_click):
        print("Here3")
