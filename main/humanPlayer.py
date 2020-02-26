from playerIntellegence import PlayerIntellegence

class HumanPlayer(PlayerIntellegence):
    
    def picking_piece(self, mouse_click):
        if not mouse_click:
            return False
        else:
            for piece in self.pieces:
                if piece.checkCollision(mouse_click.x, mouse_click.y):
                    self.selected_piece = piece
                    return True
       
    def show_possible_moves(self, mouse_click):
        return False
    
    def commit_move(self, mouse_click):
        return True
