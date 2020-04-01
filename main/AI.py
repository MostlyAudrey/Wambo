from playerIntelligence import PlayerIntelligence
from gamePiece import GamePiece
import random
from operator import attrgetter

RED = (202, 52, 51)
GREEN = (67, 124, 23)


class AI(PlayerIntelligence):
    # This counter is used to slow the AI down, so we can see how it is making its move
    wait = 0
    threshold = 5

    def __init__(self, player_color, num_pieces, piece_size, game_size, node_list, offensive=True, aggressive=True):
        PlayerIntelligence.__init__(self, player_color, num_pieces, piece_size, game_size, node_list)
        # FIXME: make these fields configurable
        self.offensive = offensive
        self.aggressive = aggressive

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

            best = None

            # Choose the game ending move, if it's a possibility
            for node in self.possible_moves:
                if node.goal == self.player_color:
                    best = node
                    break

            if best is None:
                #
                # Rank the possible moves based on position
                #   - Offensive: rank starting from the moves that make the piece
                #     move towards closest to the goal.
                #   - Defensive: do the opposite: rank based on moves that make the piece
                #     stay close to its home
                #
                if self.offensive and self.player_color == RED or \
                        not self.offensive and self.player_color == GREEN:
                    self.possible_moves.sort(key=attrgetter('label'), reverse=True)
                else:
                    self.possible_moves.sort(key=attrgetter('label'))

                #
                # Look through the newly ordered possible_moves to find the move to pick
                # based on the desired aggressiveness policy
                #
                # - Aggressive: select the first move which attacks the other player's piece,
                #   if such a move exists. Otherwise, just select the first move
                #
                # - Passive: select the first move that does not attack the other player's piece.
                #   Attacking is only a last-ditch, no-other-option option
                #
                for move in self.possible_moves:
                    if move.occupied and self.aggressive:
                        best = move
                        break

                    if not move.occupied and not self.aggressive:
                        best = move
                        break

                if best is None:
                    best = self.possible_moves[0]

            self.selected_piece.undrawBorder()
            best.remove_highlight()
            return self.selected_piece.setNode(best)

    def commit_move(self, mouse_click):
        PlayerIntelligence.undraw_possible_moves(self, self.possible_moves)
        self.selected_piece = None
        self.possible_moves = None
        return True
