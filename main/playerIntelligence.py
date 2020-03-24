from gamePiece import GamePiece

RED = (202, 52, 51)
NUM_MOVES = 2
RED_START_NODES = [3, 4]
GREEN_START_NODES = [19, 20]


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
    def compute_possible_moves(self, piece):
        node_stack = []
        nodes_to_color = []
        if piece.node:
            node_stack.append((piece.node, 0))
        else:
            start_indexes = GREEN_START_NODES
            if self.player_color == RED:
                start_indexes = RED_START_NODES
            for index in start_indexes:
                node_stack.append((self.node_list[index], 1))
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

        # These are all the accumulated possible moves
        return list(dict.fromkeys(nodes_to_color))


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
