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
    
def add_crate(board, x, y):
    board.append(["0", x, y])

def create_player(board, x, y):
    board.append(["@", x, y])
    
def check_location(board, x, y):
    for i in range(len(board)):
        if board[i][1] == x and board[i][2] == y:
            return board[i][0]
    
    return "Empty"

def player_can_move(board, x, y, direction):
    obj = check_location(board, x, y)
    
    if obj == "@":
        if direction == "up":
            target_obj = check_location(board, x, y - 1)
            if target_obj == "#":
                return False
            elif target_obj == "0" and crate_can_move(board, x, y - 1, "up") == False:
                return False
            else:
                return True
                
        
        elif direction == "down":
            target_obj = check_location(board, x, y + 1)
            if target_obj == "#":
                return False
            elif target_obj == "0" and crate_can_move(board, x, y + 1, "down") == False:
                return False
            else:
                return True
            
        elif direction == "left":
            target_obj = check_location(board, x - 1, y)
            if target_obj == "#":
                return False
            elif target_obj == "0" and crate_can_move(board, x - 1, y, "left") == False:
                return False
            else:
                return True
            
            
        elif direction == "right":
            target_obj = check_location(board, x + 1, y)
            if target_obj == "#":
                return False
            elif target_obj == "0" and crate_can_move(board, x + 1, y, "right") == False:
                return False
            else:
                return True

        
def crate_can_move(board, x, y, direction):
    obj = check_location(board, x, y)
    
    if obj == "0":
        if direction == "up":
            target_obj = check_location(board, x, y - 1)
            if target_obj != "#" and target_obj != "0":
                return True
            else:
                return False
        elif direction == "down":
            target_obj = check_location(board, x, y + 1)
            if target_obj != "#" and target_obj != "0":
                return True
            else:
                return False
        elif direction == "left":
            target_obj = check_location(board, x - 1, y)
            if target_obj != "#" and target_obj != "0":
                return True
            else:
                return False
        elif direction == "right":
            target_obj = check_location(board, x + 1, y)
            if target_obj != "#" and target_obj != "0":
                return True
            else:
                return False
            

    
def move_object(board, x, y, direction):
    obj = check_location(board, x, y)
    
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


create_player(board, 3, 2)
add_crate(board, 1, 3)
add_crate(board, 1, 2)
add_crate(board, 3, 1)
add_crate(board, 4, 2)


while True:
    player_x, player_y = get_player_xy(board)
    print("Lagerarbetarens location:\t(x = {0},y = {1})".format(player_x, player_y))
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
        
    elif direction == "d":
        print("Möjligt att flytta lagerarbetaren till höger?", end = " ")
        print(player_can_move(board, player_x, player_y, "right"))
        move_object(board, player_x, player_y, "right")

