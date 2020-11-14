def calc_rest(t, n):
    if t < n:
        return t
    elif t == n:
        return 0
    else:
        print(t, " ", n, " = ", t - n)
        return calc_rest(t-n, n)

usr_input = input("Ange täljare och nämnare:\n").split()
usr_input = list(map(int, usr_input))

print("Resten blev {}".format(calc_rest(usr_input[0], usr_input[1])))


