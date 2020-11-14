#! /usr/bin/env python3

def binary_search(lista, item, func):
    mid_index = len(lista) // 2
    mid_value = lista[mid_index]
    
    if func(mid_value) == item:
         return mid_index
     
    elif func(mid_value) > item:
        return binary_search(lista[:mid_index], item, func)
    
    elif (mid_value) < item:
        return mid_index + 1 + binary_search(lista[mid_index + 1: ], item, func)

        
    
def main():
    l1 = [1,2,3,4,5,6,7,8,9]
    print("Exempel 1")
    print("l1 = ", l1)
    print("binary_search(l1, 9, lambda x: x)")
    print("Resultat:\t", binary_search(l1, 9, lambda x: x))
    print()
    l2 = [{"name": "Anna"},{"name":"Bertil"},{"name":"Cecilia"},{"name":"David"}]
    print("Exempel 2")
    print("l2 = ", l2)
    print("""binary_search(l2, "Cecilia", lambda x: x["name"])""")
    
    print("Resultat:\t", binary_search(l2, "Cecilia", lambda x: x["name"]))
    


# ------------------------------ huvudprogram ------------------------------
if __name__ == "__main__":
    main()
