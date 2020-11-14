import random


# en lista som innehåller antal förekomster för varje sida. Sides[0] representerar då antal förekomster av sida 1
sides = []

for i in range(1,21):
    sides.append(0)

for i in range(20000):
    random_num = random.randrange(0,20)
    for j in range(len(sides)):
        if random_num == j:
            sides[j] += 1


print("{:<5}| {:}".format("sida", "antal förekomster"))
print("{:<5}+{:}".format("="*5, "="*19))
for i in range(len(sides)):
    print("{:<5}|{:>18}".format(i + 1, sides[i]))
