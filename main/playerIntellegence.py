class PlayerIntellegence:
    def player_picking_piece():
        raise NotImplementedError("Must be called on concrete child class") 

    def show_possible_moves():
        raise NotImplementedError("Must be called on concrete child class")

    def commit_move():
        raise NotImplementedError("Must be called on concrete child class")
