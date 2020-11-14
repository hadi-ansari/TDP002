#! /usr/bin/env python3

i=0
sum=0
while i <= 512:
    sum = sum+i
    i= i+1
print('Uppgift a svar: ' , sum)


multi_sum= 1;
for x in range(1, 513):
    multi_sum= multi_sum * x
print('Uppgift b svar: ')
print(multi_sum)




test_num = 1
while True:
    rest_sum = 0
    for i in range (1 , 14):
        rest_sum = rest_sum + test_num % i
        if rest_sum != 0:
            break
    if rest_sum == 0:
        break
    test_num  = test_num + 1
print('Uppgift c svar: ' , test_num)



print ('Uppgift d svar: ')
prim_sum=0
for current_num in range (3, 1001, 2):
    if (current_num  % 2) != 0 or current_num == 2:
        antal_delbar=0
        for k in range (1,current_num+1):
            if(current_num % k == 0 ):
                antal_delbar = antal_delbar + 1
        if (antal_delbar <=2):
            prim_sum = prim_sum + current_num
            print(current_num , end =" ");
print('')
print('Summan av alla dessa primtal: ' ,  end = '')
print (prim_sum)
