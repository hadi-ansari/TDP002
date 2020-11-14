#! /usr/bin/env python3

def linear_search(lista, item, func):
    for i in lista:
        if func(i) == item:
            return i;

    return None


def main():
    
    l1 = [{'title': 'Raise your voice', 'actress': 'Hilary Duff', 'score': 10}, {'title': 'Spiderman', 'actress': 'Tobey Maguire', 'score': 5}]
    print(linear_search(l1, 5, lambda x: x["score"]))

    
    l2 = ["hej","okej", "nej"]
    print(linear_search(l2, "okej", lambda x: x))    

# ------------------------------ huvudprogram ------------------------------
if __name__ == "__main__":
    main()
