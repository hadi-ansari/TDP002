from os import system, name
#clear()
lista = 0
def main():
    while True:
        
        print("\n\nVälj ett alternativ genom att skriva 1 - 5:")
        print("1. Skriv ut lista")
        print("2. Lägg till föremål i lista")
        print("3. Ta bort föremål från lista")
        print("4. Ändra ett föremål i lista")
        print("5. Avsluta programmet")
        val = input("")
        system('clear')
        if val == "1":
            visa(lista)
        elif val == "2":
            lägg_till(lista)
        elif val == "3":
            ta_bort(lista)
        elif val == "4":
            ändra(lista)
        elif val == "5":
            break
       # else:
       #     print("Du skrev in något som var fel :(")

def skapa():
    
    namn = ["penna", "kursblock", "litteratur"]
    return namn

    


def visa(lista):
    tal = 1
    print("Lista:")
    for i in lista:
        print(str(tal) + ". ", end ="")
        print(i)
        tal+=1
        
def lägg_till(lista):
    lista.append(input("Vad vill du lägga till?\n"))
    
def ta_bort(lista):
    i = int(input("Vilken rad vill du ta bort? \t"))
    i -=1
    lista.remove(lista[i])
    
def ändra(lista):
    i  = int(input("Vilken rad vill du ändra på?")) 
    lista[i - 1] = input("Skriv radens nya text:\n")

lista = skapa()
main()
