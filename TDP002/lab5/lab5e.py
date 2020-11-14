#! /usr/bin/env python3

def mirror(x):
    return x

def stars(x):
    return "*"*x

def generate_list(func, number):
    l = []
    for i in range(1, number + 1):
        l.append(func(i))
    return l

def main():
    print("Exempel för generate_list(mirror, 5):")
    print(generate_list(mirror, 5))
    print()
    print("Exempel för generate_list(stars, 5):")
    print(generate_list(stars, 5))


# ---------------- Huvudprogram ----------------- #
if __name__ == "__main__":
    main()
