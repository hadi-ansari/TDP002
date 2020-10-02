#! /usr/bin/env python3

def sum_func(x, y, func):
    s = x
    for i in range(x + 1, y + 1):
        s = func(s,i)
    return s


sum_add = sum_func(1,512, lambda x,y : x+y)
print("Summan av alla naturliga tal upp till och med 512 är:\t",sum_add)
sum_mult = sum_func(1, 512, lambda x,y : x*y)
print("{0}\n{1}".format("Produkten av alla positiva heltal upp till och med 512 är:", sum_mult))
