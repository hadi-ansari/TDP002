#! /usr/bin/env python3

def insertion_sort(l, func):
    for i in range(1, len(l)):
        el = l[i]
        for j in range(i - 1, -1 , -1):
            if func(el) <= func(l[j]):
                l.remove(el)
                l.insert(j, el)
            else:
                break
    
def main():
    l1 = [100,2,5,6,1,9,7,8]
    print("{}\n{}\nListan innan sortering:\n{}\n".format("Exempel1","="*30,l1))

    insertion_sort(l1, lambda x: x)
    print("{0}\n{1}\n{2}\n\n".format("Listan efter sortering:","insertion_sort(l1, lambda x: x)", l1))


    
    l2 = [{"name": "Anna", "age": 23},{"name":"Bertil", "age": 41},{"name":"Cecilia", "age": 37},{"name":"David", "age": 20}]
    print("{}\n{}\nListan innan sortering:\n{}\n".format("Exempel2","="*30,l2))

    insertion_sort(l2, lambda x: x["age"])
    print("{0}\n{1}\n{2}".format("Listan efter sortering:","""insertion_sort(l2, lambda x: x["age"])""", l2))


# ------------------------------ huvudprogram ------------------------------
if __name__ == "__main__":
    main()
