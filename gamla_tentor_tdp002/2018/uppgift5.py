from itertools import product

user_input = input("Mata in de siffror som ingår i koden: ")
correct_input = False

while correct_input == False:
    list_of_numbers = user_input.split()
    list_of_numbers = list(map(int, list_of_numbers))
    for i in list_of_numbers:
        if i < 0 or i > 9:
            
            correct_input = False
            break
        else:
            correct_input = True

    if correct_input == False:
        user_input = input("Felaktig inmatning. Mata in ett till fyra heltal i intervallet 1-9.\n")
    

counter = 0
all_combo = list(product(range(0,10), repeat = 4))
for combo in all_combo:
    combo_list = list(combo)
    condition = True
    for i in list_of_numbers:
        if i in combo_list:
            combo_list.remove(i)
        else:
            condition = False
            break
    if condition:
        counter += 1
    
print(counter)

