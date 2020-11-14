#! /usr/bin/env python3
from lab5g import compose
from lab5f import partial

def make_filter_map(fun1, fun2):
    map_fun2 = partial(map, fun2)
    filter_fun1 = partial(filter, fun1)
    composition =  compose(map_fun2, filter_fun1)
    return lambda x : list(composition(x))

def main():
    print("Exempel för: make_filter_map(lambda x: x % 2 == 1, lambda x: x * x)")
    print("Range är: range(10)\n")
    process = make_filter_map(lambda x: x % 2 == 1, lambda x: x * x)
    print(process(range(10)))

# ------------------ Huvudprogram ---------------------- #
if __name__ == "__main__":
    main()



