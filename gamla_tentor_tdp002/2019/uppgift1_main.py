import chess

if __name__ == '__main__':
    board = chess.create_board()
    board = chess.add_piece(board, ('a', 1), '#')
    board = chess.add_piece(board, ('a', 2), 'B')
    board = chess.add_piece(board, ('b', 1), 'S')
    board = chess.add_piece(board, ('b', 2), 'B')
    chess.print_board(board)
    print()
    board = chess.move_piece(board, ('b', 2), ('b', 3))
    board = chess.move_piece(board, ('a', 2), ('a', 4))
    chess.print_board(board)
