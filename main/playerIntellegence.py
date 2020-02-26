from gamePiece import GamePiece



class PlayerIntellegence:
    def __init__(self, player_color, num_pieces, piece_size, game_size ):
        self.pieces = []
        self.selected_piece = None
        for i in range( num_pieces ):
            self.pieces.append( GamePiece( player_color, piece_size, game_size ) )
    
    def player_picking_piece(self, mouse_click):
        raise NotImplementedError("Must be called on concrete child class") 

    def show_possible_moves(self, mouse_click):
        raise NotImplementedError("Must be called on concrete child class")

    def commit_move(self, mouse_click):
        raise NotImplementedError("Must be called on concrete child class")
