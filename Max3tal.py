#! /usr/bin/env python3

first_num = int(input('Mata in det  första talet: '))
second_num = int(input('Mata in det andra  talet: '))
third_num = int(input('Mata in det tredje talet: '))

max_num = first_num

if max_num < second_num:
    max_num = second_num
if max_num < third_num:
    max_num = third_num
print('Det största talet är: ', max_num)
