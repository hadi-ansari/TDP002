import sys, re

usr_input = sys.argv[1:]
usr_input = " ".join(usr_input)

usr_input = re.sub("[aA]", "4", usr_input)
usr_input = re.sub("[eE]", "3", usr_input)
usr_input = re.sub("[oO]", "0", usr_input)
usr_input = re.sub("[lL]", "1", usr_input)
usr_input = re.sub("[tT]", "7", usr_input)

lista = list(usr_input)

do_upper = False
for i in range(len(lista)):
    if re.match("[a-z]", lista[i]) != None:
        if do_upper:
            lista[i] = lista[i].upper()
            do_upper = False
        else:
            do_upper = True

            

print("".join(lista))

