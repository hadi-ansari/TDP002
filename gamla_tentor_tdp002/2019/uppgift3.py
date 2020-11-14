def draw_mountain(height):
    for i in range(height):
        left_space = " " * (height - 1 - i)
        space_middle = " " * 2 * i 
        print("{}/{}\\".format(left_space, space_middle))





def main():
    height = int(input("Mata in storleken på berget: "))
    draw_mountain(height)

    
if __name__ == "__main__":
    main()
