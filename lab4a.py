#! /usr/bin/env python3
import os

def create_board():
    board = []
    return board

def display_board(board):
    max_y = 0
    for m in range(len(board)):
        if board[m][2] > max_y:
            max_y = board[m][2]


    
    for i in range(max_y + 1):
        max_x = 0
        for j in range(len(board)):
            if board[j][2] == i and board[j][1] > max_x:
                max_x = board[j][1]

        for y in range(max_x + 1):
            condition = False
            for z in range(len(board)):
                if board[z][1] == y and board[z][2] == i:
                    print(board[z][0], end = "")
                    condition = True

            if condition == False:
                print(" ", end = "")
                
                
        print()

        

def add_wall(board, x, y):
    board.append(["#", x, y])
    
def add_box(board, x, y):
    board.append(["o", x, y])

def create_player(board, x, y):
    board.append(["@", x, y])
    
def check_location(board, x, y):
    for i in range(len(board)):
        if board[i][1] == x and board[i][2] == y:
            return board[i][0]
    
    return "Empty"

def move_object(board, x, y, direction):
    obj = check_location(board, x, y)

    if obj == "@":
        if direction == "up":
            target_obj = check_location(board, x, y - 1)
            if target_obj == "Empty":
                board.append(["@", x , y - 1])
                board.remove(["@", x, y])
            elif target_obj == "0":
                target_obj2 = check_location(board, x, y - 2)
                if target_obj2 == "Empty":
                    board.append(["@", x , y - 1])
                    board.remove(["@", x, y])

                    board.append(["0", x , y - 2])
                    board.remove(["0", x, y - 1])
                elif target_obj2 == ".":
                    board.append(["@", x , y - 1])
                    board.remove(["@", x, y])

                    board.append(["*", x , y - 2])
                    board.remove(["o", x, y - 1])
            elif target_obj == ".":
                board.append(["+", x , y - 1])
                board.remove(["@", x, y])                
                    
                
                
        elif direction == "down":
            target_obj = check_location(board, x, y + 1)
            if target_obj == "Empty":
                board.append(["@", x, y + 1])
                board.remove(["@", x, y])

        elif direction == "right":
            target_obj = check_location(board, x + 1, y)
            if target_obj == "Empty":
                board.append(["@", x + 1, y])
                board.remove(["@", x, y])
                
        elif direction == "left":
            target_obj = check_location(board, x - 1, y)
            if target_obj == "Empty":
                board.append(["@", x - 1, y])
                board.remove(["@", x, y])
                    
                
    elif obj == "o":
        if direction == "up":
            target_obj = check_location(board, x, y - 1)
            if target_obj == "Empty":
                board.append(["@", x , y - 1])
                board.remove(["@", x, y])
                
        elif direction == "down":
            target_obj = check_location(board, x, y + 1)
            if target_obj == "Empty":
                board.append(["@", x, y + 1])
                board.remove(["@", x, y])

        elif direction == "right":
            target_obj = check_location(board, x + 1, y)
            if target_obj == "Empty":
                board.append(["@", x + 1, y])
                board.remove(["@", x, y])
                
        elif direction == "left":
            target_obj = check_location(board, x - 1, y)
            if target_obj == "Empty":
                board.append(["@", x - 1, y])
                board.remove(["@", x, y])

#def get_position(board,)

    
# ======================================================================
# Huvudprogram
# ======================================================================
board = create_board()

add_wall(board, 0, 0)
add_wall(board, 1, 0)
add_wall(board, 2, 0)
add_wall(board, 3, 0)
add_wall(board, 4, 0)
add_wall(board, 5, 0)

add_wall(board, 0, 1)
add_wall(board, 0, 2)
add_wall(board, 0, 3)
add_wall(board, 0, 4)

add_wall(board, 5, 1)
add_wall(board, 5, 2)
add_wall(board, 5, 3)
add_wall(board, 5, 4)

add_wall(board, 1, 4)
add_wall(board, 2, 4)
add_wall(board, 3, 4)
add_wall(board, 4, 4)


create_player(board, 2, 3)
add_box(board, 2, 2)
display_board(board)


move_object(board, 2, 3, "up")
display_board(board)






