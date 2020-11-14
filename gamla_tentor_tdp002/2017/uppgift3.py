import random, math

c_area = 0.0
s_area = 0.0
s = 2.0
r = 1.0
counter = 1
for i in range(1000000000):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    if counter == 10000000:
        pi = (s**2 * c_area) / (r**2 * s_area)
        print("{}\t{:0.6f}".format(i + 1, pi))
        counter = 0
    dis = math.sqrt(x**2 + y**2)
    if dis <= r:
        c_area += 1.0
        s_area += 1.0
    else:
        s_area += 1.0
    counter +=1
