from itertools import cycle, repeat

b = "ABC"
p = []
days1 = [5, 10, 3, 2]
days = [5, 10, 3, 2]

mx_d = 0
for j in range(len(days)):
    if j + 1 + days[j] > mx_d:
        mx_d = j + 1 + days[j]


# d = {"A": [3], "B": [2], "C": [1]}


# cond = True
# for i in range(len(b) - 1, mx_d + 1):
#     if cond:
#         for k in b:
#             p.append(k)
#         cond = False
        

# print("".join(p))

