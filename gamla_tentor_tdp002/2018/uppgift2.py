from itertools import product 


def create_dice(sides):
    dice = []
    for i in range(sides):
        dice.append( i+1 )
    return dice




number_of_dices = int(input("Mata in antalet tärningar:\n"))
number_of_sides = int(input("Mata in antalet sidor för tärningarna:\n"))
highest_sum = number_of_sides * number_of_dices
lowest_sum = number_of_dices

dice = create_dice(number_of_sides)


d = {}
for i in range(lowest_sum,  highest_sum+1):
    d[i] = ""
        
res = list(product(range(1, number_of_sides + 1), repeat = number_of_dices))

for item in res:
    for key in d:
        if key == sum(item):
            d[key] += "*"
            break

print("Resultat:")   
for i in d:
    print("{:<4}{}".format(i, d[i]))
