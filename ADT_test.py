def create_character(speed, power, learn_spel = False):
    if learn_spel:
        char = {"Speed": speed, "Power": power, "Learn_magic": learn_spel, "Spels": []}
    else:
        char = {"Speed": speed, "Power": power, "Learn_magic": learn_spel}
    return char

def add_spel(char, spel):
    if char["Learn_magic"]:
        char["Spels"].append(spel)

Wizard = create_character(5, 5, True)
Fighter = create_character(6, 4)

print(Wizard)
print(Fighter)

print()
add_spel(Wizard, "Rage")
add_spel(Fighter, "Heal")
print(Wizard)
print(Fighter)


