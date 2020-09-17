#! /usr/bin/env python3
import os

def create_board():
    board = []
    return board

def get_max_x(board, j):
    max_x = 0
    for i in range(len(board)):
        if board[i][2] == j and board[i][1] > max_x:
            max_x = board[i][1]
    return max_x

def get_max_y(board):
    max_y = 0
    for i in range(len(board)):
        if board[i][2] > max_y:
            max_y = board[i][2]
    return max_y

def display_board(board):
    max_y = get_max_y(board)
    
    for i in range(max_y + 1):
        max_x = get_max_x(board, i)
        for j in range(max_x + 1):
            symbol = get_symbol(board, j, i)
            print(symbol, end = "")

        print()
        
def add_wall(board, x, y):
    board.append(["#", x, y])
    
def add_crate(board, x, y):
    board.append(["0", x, y])

def create_player(board, x, y):
    board.append(["@", x, y])
    
def add_storage(board, x, y):
    board.append([".", x, y])
    
def get_symbol(board, x, y):
    for i in range(len(board)):
        if board[i][1] == x and board[i][2] == y:
            return board[i][0]
        
    return " "

def player_can_move(board, x, y, direction):
    obj = get_symbol(board, x, y)
    
    if obj == "@":
        if direction == "up":
            target_obj = get_symbol(board, x, y - 1)
            if target_obj == "#":
                return False
            elif target_obj == "0" and crate_can_move(board, x, y - 1, "up") == False:
                return False
            else:
                return True
                
        
        elif direction == "down":
            target_obj = get_symbol(board, x, y + 1)
            if target_obj == "#":
                return False
            elif target_obj == "0" and crate_can_move(board, x, y + 1, "down") == False:
                return False
            else:
                return True
            
        elif direction == "left":
            target_obj = get_symbol(board, x - 1, y)
            if target_obj == "#":
                return False
            elif target_obj == "0" and crate_can_move(board, x - 1, y, "left") == False:
                return False
            else:
                return True
            
            
        elif direction == "right":
            target_obj = get_symbol(board, x + 1, y)
            if target_obj == "#":
                return False
            elif target_obj == "0" and crate_can_move(board, x + 1, y, "right") == False:
                return False
            else:
                return True

        
def crate_can_move(board, x, y, direction):
    obj = get_symbol(board, x, y)
    
    if obj == "0":
        if direction == "up":
            target_obj = get_symbol(board, x, y - 1)
            if target_obj != "#" and target_obj != "0":
                return True
            else:
                return False
        elif direction == "down":
            target_obj = get_symbol(board, x, y + 1)
            if target_obj != "#" and target_obj != "0":
                return True
            else:
                return False
        elif direction == "left":
            target_obj = get_symbol(board, x - 1, y)
            if target_obj != "#" and target_obj != "0":
                return True
            else:
                return False
        elif direction == "right":
            target_obj = get_symbol(board, x + 1, y)
            if target_obj != "#" and target_obj != "0":
                return True
            else:
                return False
            

    
def move_object(board, x, y, direction):
    obj = get_symbol(board, x, y)
    
    if obj == "@" and player_can_move(board, x, y, direction):
        if direction == "up":
            move_object(board, x , y - 1, "up")
            board.append(["@", x , y - 1])
            board.remove(["@", x, y])
                    
        elif direction == "down":
            move_object(board, x, y + 1, "down")
            board.append(["@", x, y + 1])
            board.remove(["@", x, y])

        elif direction == "right":
            move_object(board, x + 1, y , "right")
            board.append(["@", x + 1, y])
            board.remove(["@", x, y])
                
        elif direction == "left":
            move_object(board, x - 1, y , "left")
            board.append(["@", x - 1, y])
            board.remove(["@", x, y])
                    
                
    elif obj == "0" and crate_can_move(board, x, y, direction):
        if direction == "up":
            board.append(["0", x , y - 1])
            board.remove(["0", x, y])
        elif direction == "down":
            board.append(["0", x , y + 1])
            board.remove(["0", x, y])
        elif direction == "right":
            board.append(["0", x + 1, y])
            board.remove(["0", x, y])
        elif direction == "left":
            board.append(["0", x - 1, y])
            board.remove(["0", x, y])
            

def get_player_xy(board):
    for i in range(len(board)):
        if board[i][0] == "@" or board[i][0] == "+":
            return board[i][1], board[i][2]

def upgrade_board(board):
    for i in range(len(board) - 1):
        for j in range(i + 1, len(board)):
            if board[i][1] == board[j][1] and board[i][2] == board[j][2]:
                print("Jag kommer in här!!!")
                obj1 = board[i][0]
                obj2 = board[j][0]
                if obj1 == "@":
                    board[i][0] = "+"
                    board.remove([".", board[j][1], board[j][2]])
                elif obj2 == "@":
                    board[j][0] = "+"
                    board.remove([".", board[i][1], board[i][2]])
                elif obj1 == "0":
                    board[i][0] = "*"
                    board.remove([".", board[j][1], board[j][2]])
                elif obj2 == "0":
                    board[j][0] = "*"
                    board.remove([".", board[i][1], board[i][2]])
    
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

add_wall(board, 5, 1)
add_wall(board, 5, 2)
add_wall(board, 5, 3)

add_wall(board, 0, 4)
add_wall(board, 1, 4)
add_wall(board, 2, 4)
add_wall(board, 3, 4)
add_wall(board, 4, 4)
add_wall(board, 5, 4)



create_player(board, 4, 2)
add_crate(board, 3, 2)
add_storage(board, 1, 2)
# add_crate(board, 3, 1)
# add_crate(board, 4, 2)


while True:
    player_x, player_y = get_player_xy(board)
    print("Lagerarbetarens position:\t(x = {0},y = {1})".format(player_x, player_y))
    upgrade_board(board)
    display_board(board)
    direction = input()
    if direction == "w":
        print("Möjligt att flytta lagerarbetaren uppåt?", end = " ")
        print(player_can_move(board, player_x, player_y, "up"))
        move_object(board, player_x, player_y, "up")
        
    elif direction == "s":
        print("Möjligt att flytta lagerarbetaren nedåt?", end = " ")
        print(player_can_move(board, player_x, player_y, "down"))
        move_object(board, player_x, player_y, "down")
        
    elif direction == "a":
        print("Möjligt att flytta lagerarbetaren till vänster?", end = " ")
        print(player_can_move(board, player_x, player_y, "left"))
        move_object(board, player_x, player_y, "left")

        print(board)
    elif direction == "d":
        print("Möjligt att flytta lagerarbetaren till höger?", end = " ")
        print(player_can_move(board, player_x, player_y, "right"))
        move_object(board, player_x, player_y, "right")

