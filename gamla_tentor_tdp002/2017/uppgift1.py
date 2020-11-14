print("Mata in talen:")
input_numbers = []
input_sum = "0"
while True:
    inp = input()
    inp = inp.replace(" ","")
    if all(elem in "-" for elem in inp):
        input_sum = input()
        input_sum = input_sum.replace(" ","")
        break
    input_numbers.append(inp)
    
input_numbers = list(map(int, input_numbers))
sum_of_numbers=sum(input_numbers)
if sum_of_numbers != int(input_sum):
    print("Summan är felaktig")
else:
    print("Summan är korrekt")

