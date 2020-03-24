from gamePiece import GamePiece


class PlayerIntelligence:
    def __init__(self, player_color, num_pieces, piece_size, game_size, node_list):
        self.pieces = []
        self.selected_piece = None
        self.possible_moves = None
        self.game_size = game_size
        self.player_color = player_color
        self.node_list = node_list
        for i in range(num_pieces):
            self.pieces.append(GamePiece(player_color, piece_size, game_size))

    # Compute all the possible moves that can be made given the current position of all
    # the player pieces
    def compute_possible_moves(self):
        pass

    def player_picking_piece(self, mouse_click):
        raise NotImplementedError("Must be called on concrete child class")

    def show_possible_moves(self, mouse_click):
        raise NotImplementedError("Must be called on concrete child class")

    def commit_move(self, mouse_click):
        raise NotImplementedError("Must be called on concrete child class")

    def game_over(self, mouse_click):
        if mouse_click:
            return 4
        return 0
