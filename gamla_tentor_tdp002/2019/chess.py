def create_board():
    chess_board = []
    char = "a"
    for i in range(1, 9):
        for j in range (1, 9):
            chess_board.append([char, j])
        char = chr(ord(char) + 1)

    return chess_board

def print_board(board):
    for item in board:
        if len(item) == 3:
            print("({}, {}) : {}".format(item[0], item[1], item[2])) 

def add_piece(board, spot, obj):
    for item in board:
        if item[0] == spot[0] and item[1] == spot[1]:
            item.append(obj)
    return board

def move_piece(board, old_spot, new_spot):
    for item in board:
        if item[0] == old_spot[0] and item[1] == old_spot[1]:
            new_item = []
            new_item.append(new_spot[0])
            new_item.append(new_spot[1])
            if len(item) == 3:
                new_item.append(item[2])
            board.remove(item)
            board.append(new_item)

    board.sort(key = lambda x: x[0])
    return board
