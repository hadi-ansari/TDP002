#! /usr/bin/env python3

first_price = int(input("Första pris:\t"))
last_price = int(input("Sista pris:\t"))
step = float(input("Steg:\t"))
moms_procent = int(input("Momsprocent:\t"))

print("\n=== Momstabell ===")
print("{:<19}{:<9}{}".format("Pris utan moms", "Moms", "Pris med moms"))


current_price = first_price
current_moms = moms_procent * first_price / 100
current_with_moms = current_price + current_moms
space = " "*5

while current_price <= last_price:
    print("{}{:0.2f}{:>9}{:0.2f}{:>9}{:0.2f}".format(space, current_price, space, current_moms, space, current_with_moms))
    current_price += step
    current_moms = moms_procent * current_price / 100
    current_with_moms = current_moms + current_price
    print()
    
