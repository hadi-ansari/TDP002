def skapa():
    namn = ["penna", "kursblock", "litteratur"]
    return namn

def visa(lista):
    tal = 1
    for i in lista:
        print(str(tal) + ". ", end ="")
        print(i)
        tal+=1
        
def lägg_till(lista):
    lista.append(input("Vad vill du lägga till?\n"))
    
def ta_bort(lista):
    i = int(input("Vilken rad vill du ta bort?"))
    i -=1
    lista.remove(lista[i])
    
def ändra(lista):
    i  = int(input("Vilken rad vill du ändra på?")) 
    lista[i - 1] = input("Skriv radens nya text:\n")

#minlista = lista_skapa()
#lista_visa(minlista)


