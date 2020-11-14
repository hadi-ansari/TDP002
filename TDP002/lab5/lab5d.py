#! /usr/bin/env python3
import os
from os import listdir, getcwd, chdir
from colorama import Fore, Back, Style

def pwd():
    current_path = getcwd()
    print(current_path)

def cd(command):
    try:
        target_dir = command[3:]
        chdir(target_dir)
        
    except Exception as e:
        print(e)

def ls():
    item_list = listdir()
    for i in item_list:
        if os.path.isdir(i):
            print(Fore.BLUE + i + Fore.WHITE)
        else:
            print(i)

def cat(command):
    try:
        target_file = command[4:]
        with open(target_file, "r") as f:
            content = f.read()
            print(content)
            
    except Exception as e:
        print(e)
        
def clear():
    os.system("clear")
    
def main():
    while True:
        command = input(Fore.GREEN + "Command>>" + Fore.WHITE)
        if command == "pwd":
            pwd()
        elif "cd"== command.split()[0]:
            cd(command)
        elif command == "ls":
            ls()
        elif "cat" == command.split()[0]:
            cat(command)

        elif command.upper() == "CLEAR":
            clear()
        elif command == "x":
            break
# ------------- Huvudprogram ------------- #
main()
