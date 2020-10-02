#! /usr/bin/env python3

def contain(element, l):
    for i in l:
        if element == i:
            return True
    
    return False

def main():
    haystack = 'Can you find the needle in this haystack?'.split()
    print("""Exempel som kontrollerar om "Can" finns i:\n""", haystack)
    print(contain("Can", haystack))
# -------------- Huvudprogram --------------- #
if __name__ == "__main__":
    main()

