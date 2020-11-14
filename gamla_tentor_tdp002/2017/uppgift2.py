N = input("Mata in N: ")

operations = []
for i in range(3):
    operations.append(input())

for i in operations:
    if i == "DUP":
        N += N[-1]
    elif i == "ROT":
        new_N = N[-1] + N[:-1]
        N = new_N
print("N blev {}.".format(N))
