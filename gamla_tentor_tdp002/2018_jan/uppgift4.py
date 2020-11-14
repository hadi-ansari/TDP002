import sys

args = sys.argv[1:]

if len(args) == 0:
    print("Ingen fil angavs!")

fil = args[0]
numbers = []

found = False
found_obj = []

with open(fil , "r") as f:
    for line in f:
        l = line.split()
        if len(l) != 0:
            print(l)
            for i in l:
                numbers.append(i)
                lenght_numbers = len(numbers)
                numbers = list(dict.fromkeys(numbers))
                if len(numbers) != lenght_numbers:
                    found = True
                    found_obj = i
        if found:
            break
                
        
if found:
    print("Siffran {} var en dubbelt".format(found_obj))
else:
    print("Filen innehöll ingen dubblett.")
