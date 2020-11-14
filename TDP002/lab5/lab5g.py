#! /usr/bin/env python3

def multiply_five(n):
    return n * 5

def add_ten(x):
    return x + 10
    



def compose(F_a, F_b):
    F_res = lambda x : F_a(F_b(x))
    
    return F_res

def main():
    composition = compose(multiply_five, add_ten)
    print("Exempel för composition(3):")
    print(composition(3))
    print()
    print("Exempel för composition(0):")
    print(composition(0))
    
    
# ------------- Huvudprogram -------------- #
if __name__ == "__main__":
    main()
