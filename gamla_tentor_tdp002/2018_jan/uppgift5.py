import random

def rand_white():
    num = random.randrange(0,3)
    if num == 0:
        return " "
    elif num == 1:
        return "\t"
    else:
        return "\n"


amounts = 5
fil = "duplicate.txt"
dup = True
d_number = 19

if dup:
    amounts -= 2



lista = []
for i in range(amounts):
        num = random.randrange(1, 10001)
        lista.append(num)

inx1 = random.randrange(0, len(lista))
if inx1 != len(lista) - 1:
        lista.insert(inx1, d_number)
else:
        lista.append(d_number)
        
inx2 = random.randrange(0, len(lista))
if inx2 != len(lista) - 1:
        lista.insert(inx2, d_number)
else:
        lista.append(d_number)



lista = map(str, lista)
with open(fil, "w") as f:
    for i in lista:
        f.write(i)
        for k in range(10):
            f.write(rand_white())
    f.write("\n")
