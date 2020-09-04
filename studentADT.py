#! /usr/bin/env python3

def create_student(name = "", liu_id = ""):
    student = {"Name" : name, "Liu_Id" : liu_id}
    
    return student

def change_details(student):
    item = input("Vad vill du ändra på?\n1. Namn\n2. Lid ID\n")
    if item == "1":
        new_name = input("Skriv nya namnet:\t")
        student["Name"] = new_name
    elif item == "2":
        new_liu_id = input("Skriv nya Liu ID:\t")
        student["Liu_Id"] = new_liu_id
    

def show_student(student):
    print("{:<10}\t{:<10}".format(student["Name"], student["Liu_Id"]))

