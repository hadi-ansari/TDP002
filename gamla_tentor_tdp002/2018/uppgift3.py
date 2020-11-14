import re

string = input("Mata in en fras på rövarspråket: ")

l1 = string.split()
decrypted_word = ""
decrypted_list = []

for i in l1:
    decrypted_word = i
    k = i
    match = re.findall(r"[^aeioyåäö]{1}o[^aeioyåäö]{1}", i)
    match = list(dict.fromkeys(match))
    for j in match:
        decrypted_word  = re.sub(j, j[0], k)
        k = decrypted_word 
    decrypted_list.append(decrypted_word)
    decrypted_word = ""
    
print("Frasen på svenska: ", end =" ")
for i in decrypted_list:
    print(i , end =" ")
print()
