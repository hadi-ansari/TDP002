#! /usr/bin/env python3
def add (n, m):
    return n + m 

def partial(fun, arg):
    return lambda x : fun(arg, x)

def main():
    add_five = partial(add, 5)
    print("Exempel för add_five(1):")
    print(add_five(1))
    
# ----------- Huvudprogram ---------- #
if __name__ == "__main__":
    main()
