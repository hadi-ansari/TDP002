#! /usr/bin/env python3

from studentADT import *

def add_student (data_base):
    student_name = input("Vad heter studenten:\t")
    student_liu_id = input("Skriv studentens Liu ID:\t")
    new_student = create_student(student_name, student_liu_id)
    data_base.append(new_student)

def show_data_base (data_base):
    counter = 1
    print("="*25)
    print("{:<10}\t{:<10}".format("Name", "Liu ID"))
    print("="*25)
    for i in data_base:
        print(counter,". " , end = "")
        show_student(i)
        counter +=1
    print()

def fill_data_base():
    s1 = create_student("Hadi","hadan326")
    s2 = create_student("Julia","jular703")
    s3 = create_student("Ali","algho456")
    s4 = create_student("Simon","siman453")
    my_list = [s1, s2, s3, s4]
    return my_list
    
def main():

    data_base = fill_data_base()


    while True:
        print("Välkommen till student databas")
        print("1. Visa listan\n2. Skapa ny student\n3. Ta bort en student\n4. Hitta en student\n5. Avstula")
        select = int(input())

        if select == 1:
            show_data_base(data_base)
        elif select == 2:
            add_student(data_base)
        elif select == 5:
            break
        
#    elif select == 3:
        

main()
