#! /usr/bin/env python3
import os
from os import listdir
import sys

def create_board():
    board = []
    return board
def check_level_files():
    return 0
def load_board(doc):
    board = create_board()
    os.chdir("levels")
    with open(doc, "r") as f:
      
        
        current_x = 0
        current_y = 0
        for line in f:
            for letter in line:
                if letter == "#":
                    add_wall(board, current_x, current_y)
                elif letter == "o":
                    add_crate(board, current_x, current_y)
                elif letter == "@":
                    create_player(board, current_x, current_y)
                elif letter == ".":
                    add_storage(board, current_x, current_y)
                current_x += 1
            current_y += 1
            current_x = 0

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
    board.append(["o", x, y])

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
    
    if obj == "@" or obj == "+":
        if direction == "up":
            target_obj = get_symbol(board, x, y - 1)
            if target_obj == "#":
                return False
            elif (target_obj == "o" or target_obj == "*") and crate_can_move(board, x, y - 1, "up") == False:
                return False
            else:
                return True
                
        
        elif direction == "down":
            target_obj = get_symbol(board, x, y + 1)
            if target_obj == "#":
                return False
            elif (target_obj == "o" or target_obj == "*") and crate_can_move(board, x, y + 1, "down") == False:
                return False
            else:
                return True
            
        elif direction == "left":
            target_obj = get_symbol(board, x - 1, y)
            if target_obj == "#":
                return False
            elif (target_obj == "o" or target_obj == "*") and crate_can_move(board, x - 1, y, "left") == False:
                return False
            else:
                return True
            
            
        elif direction == "right":
            target_obj = get_symbol(board, x + 1, y)
            if target_obj == "#":
                return False
            elif (target_obj == "o" or target_obj == "*") and crate_can_move(board, x + 1, y, "right") == False:
                return False
            else:
                return True

        
def crate_can_move(board, x, y, direction):
    obj = get_symbol(board, x, y)
    
    if obj == "o" or obj == "*":
        if direction == "up":
            target_obj = get_symbol(board, x, y - 1)
            if target_obj != "#" and target_obj != "o" and target_obj != "*":
                return True
            else:
                return False
        elif direction == "down":
            target_obj = get_symbol(board, x, y + 1)
            if target_obj != "#" and target_obj != "o" and target_obj != "*":
                return True
            else:
                return False
        elif direction == "left":
            target_obj = get_symbol(board, x - 1, y)
            if target_obj != "#" and target_obj != "o" and target_obj != "*":
                return True
            else:
                return False
        elif direction == "right":
            target_obj = get_symbol(board, x + 1, y)
            if target_obj != "#" and target_obj != "o" and target_obj != "*":
                return True
            else:
                return False
            

    
def move_object(board, x, y, direction):
    obj = get_symbol(board, x, y)
    
    if (obj == "@" or obj == "+") and player_can_move(board, x, y, direction):
        if direction == "up":
            move_object(board, x , y - 1, "up")
            symbol = next_symbol(board, x, y, direction)
            if obj == "+":
                board.append([".", x, y])
            if symbol == "+":
                board.remove([".", x, y - 1])
            board.remove([obj, x, y])
            board.append([symbol, x, y - 1])
                    
        elif direction == "down":
            move_object(board, x, y + 1, "down")
            symbol = next_symbol(board, x, y, direction)
            if obj == "+":
                board.append([".", x, y])
            if symbol == "+":
                board.remove([".", x, y + 1])
            board.remove([obj, x, y])
            board.append([symbol, x, y + 1])

        elif direction == "right":
            move_object(board, x + 1, y , "right")
            symbol = next_symbol(board, x, y, direction)
            if obj == "+":
                board.append([".", x, y])
            if symbol == "+":
                board.remove([".", x + 1, y])
            board.remove([obj, x, y])
            board.append([symbol, x + 1, y])
                
        elif direction == "left":
            move_object(board, x - 1, y , "left")
            symbol = next_symbol(board, x, y, direction)
            if obj == "+":
                board.append([".", x, y])
            if symbol == "+":
                board.remove([".", x - 1, y])
            board.remove([obj, x, y])
            board.append([symbol, x - 1, y])
            
                    
                
    elif (obj == "o" or obj == "*") and crate_can_move(board, x, y, direction):
        if direction == "up":
            symbol = next_symbol(board, x, y, direction)
            if obj == "*":
                board.append([".", x, y])
            if symbol == "*":
                board.remove([".", x, y - 1])
            board.remove([obj, x, y])
            board.append([symbol, x, y - 1])
        elif direction == "down":
            symbol = next_symbol(board, x, y, direction)
            if obj == "*":
                board.append([".", x, y])
            if symbol == "*":
                board.remove([".", x, y + 1])
            board.remove([obj, x, y])
            board.append([symbol, x, y + 1])
        elif direction == "right":
            symbol = next_symbol(board, x, y, direction)
            if obj == "*":
                board.append([".", x, y])
            if symbol == "*":
                board.remove([".", x + 1, y])
            board.remove([obj, x, y])
            board.append([symbol, x + 1, y])
        elif direction == "left":
            symbol = next_symbol(board, x, y, direction)
            if obj == "*":
                board.append([".", x, y])
            if symbol == "*":
                board.remove([".", x - 1, y])
            board.remove([obj, x, y])
            board.append([symbol, x - 1, y])
            

def get_player_xy(board):
    for i in range(len(board)):
        if board[i][0] == "@" or board[i][0] == "+":
            return board[i][1], board[i][2]

def next_symbol(board, x, y, direction):
    obj = get_symbol(board, x, y)

    if (obj == "@" or obj == "+") and direction == "up":
        target_obj = get_symbol(board, x, y - 1)
        if target_obj == ".":
            return "+"
        else:
            return "@"
    elif (obj == "@" or obj == "+") and direction == "down":
        target_obj = get_symbol(board, x, y + 1)
        if target_obj == ".":
            return "+"
        else:
            return "@"
    elif (obj == "@" or obj == "+") and direction == "right":
        target_obj = get_symbol(board, x + 1, y)
        if target_obj == ".":
            return "+"
        else:
            return "@"
    
    elif (obj == "@" or obj == "+") and direction == "left":
        target_obj = get_symbol(board, x - 1, y)
        if target_obj == ".":
            return "+"
        else:
            return "@"

    if (obj == "o" or obj == "*") and direction == "up":
        target_obj = get_symbol(board, x , y - 1)
        if target_obj == ".":
            return "*"
        else:
            return "o"
    if (obj == "o" or obj == "*") and direction == "down":
        target_obj = get_symbol(board, x , y + 1)
        if target_obj == ".":
            return "*"
        else:
            return "o"
    if (obj == "o" or obj == "*") and direction == "right":
        target_obj = get_symbol(board, x + 1, y)
        if target_obj == ".":
            return "*"
        else:
            return "o"
    if (obj == "o" or obj == "*") and direction == "left":
        target_obj = get_symbol(board, x - 1, y)
        if target_obj == ".":
            return "*"
        else:
            return "o"
def is_over(board):
    for i in range(len(board)):
        if board[i][0] == "o":
            return False
    return True

def main():
    levels = sorted(os.listdir("levels"))
    for i in range (len(levels)):
        print(levels[i])
    select = int(input("Välj en nivå: "))
    board = load_board(levels[select-1])
   

    while True:
        print("För att flytta lagerarbetaren uppåt (w), nedåt (s), till höger (d), vänster (a)")
        player_x, player_y = get_player_xy(board)
        display_board(board)
        if is_over(board):
            print("Du har vunnit!!!!!!!!!!!!!!!!")
            break
        direction = input()
        if direction == "w":
            move_object(board, player_x, player_y, "up")
        
        elif direction == "s":
            move_object(board, player_x, player_y, "down")
        
        elif direction == "a":
            move_object(board, player_x, player_y, "left")

        elif direction == "d":
            move_object(board, player_x, player_y, "right")
        os.system("clear")
    
# ======================================================================
# Huvudprogram
# ======================================================================

main()




   

