#! /usr/bin/env python3
#-*- coding: utf-8 -*-

name = input('Vad heter du? ')
print('Hej ', end = '')
print(name)
age = int(input('Mata in din ålder: '))
print('Du föddes år ' , end = '')
current_year=2020
birth_year = current_year - age
print(birth_year)
region = input('Vilket län föddes du i? ')
name_half_len = int(len(name)/2)
region_half_len = int(len(region)/2)
combination = name[0:name_half_len] + region[region_half_len: len(region)]
print('Första halvan av ditt namn och andra halvan av ditt lär är:')
print(combination)
