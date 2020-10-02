#! /usr/bin/env python3

def db_search(db, key, value):
    found = []
    for i in range(len(db)):
        if db[i][key] == value:
            found.append(db[i])
    return found
def main():
    db = [
        {'name': 'Jakob', 'position': 'assistant'},
        {'name': 'Åke', 'position': 'assistant'},
        {'name': 'Ola', 'position': 'examiner'},
        {'name': 'Henrik', 'position': 'assistant'}
    ]
    
    print("Databasen:\n")
    for i in db:
        print (i)
    print()
    print("Detta är ett exempel på sökningen för namnet Jakob:")
    found = db_search(db, "name", "Jakob")
    print(found)
    found.clear()
    print()
    print("Detta är ett exempel på sökningen för post assistant:")
    found = db_search(db, "position", "assistant")
    print(found)

#---------- Huvudprogram ----------------#
if __name__ == "__main__":
    main()
