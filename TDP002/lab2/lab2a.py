def frame(text):
    print("*" * (len(text) + 4))
    print("*", text,"*")
    print("*" * (len(text) + 4))

def triangle(tal):
    for i in range (tal):
        print("*", end ="")
        print("*" * 2 * i)

def flag(tal):

    for i in range(tal * 8):
        if ( i == tal * 8 / 2):
            print ("")
            
        print("*" * tal * 10, "*" * tal * 10)
    
text_frame = input("skriv en text")
frame(text_frame)
tal_triangle = int(input("skriv ett tal"))
triangle(tal_triangle)
tal_flag = int(input("skriv ett tal"))
flag(tal_flag)
