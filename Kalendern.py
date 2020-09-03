#! /usr/bin/env python3

def receive_info():
    day_condition = False
    month_condition = False


    while day_condition == False :
        week_day = int(input("Mata in första veckodagen:\t"))
        if week_day > 7 or week_day < 1:
            print ("\nOrimlig veckodag! Vänligen kontrollera och försök igen.\n")
        else:
            day_condition = True


    while month_condition == False:
        number_of_days = int(input("Mata in antalet dagar i månaden:\t"))
        if number_of_days > 31 or number_of_days < 28:
            print ("\nOrimlig antal dagar i månaden! Vänligen kontrollera och försök igen.\n")
        else:
            month_condition = True
    return week_day, number_of_days

            

def month_print(week_day, number_of_days):
    current_day = week_day
    print("må ti on to fr lö sö")

    if week_day == 1:
        for i in range (1, number_of_days + 1 ):
            if i < 10:
                print ("", i, end = " ")
            else:
                print (i ,  end = " ")
            if  current_day  == 7 and i != number_of_days:
                current_day = 0
                print()
            current_day += 1

    elif week_day == 2:
        print (" "*2 , end = " ")
        for i in range (1, number_of_days + 1 ):
            if i < 10:
                print ("", i, end = " ")
            else:
                print (i ,  end = " ")
            if current_day == 7 and i != number_of_days:
                current_day = 0
                print()
            current_day += 1

    elif week_day == 3:
        print (" "*5, end = " ")
        for i in range (1, number_of_days + 1 ):
            if i < 10:
                print ("", i, end = " ")
            else:
                print (i ,  end = " ")
            if current_day == 7 and i != number_of_days:
                current_day = 0
                print()
            current_day += 1
        
    elif week_day == 4:
        print(" "*8 , end = " " )
        for i in range (1, number_of_days + 1 ):
            if i < 10:
                print ("", i, end = " ")
            else:
                print (i ,  end = " ")
            if current_day == 7 and i != number_of_days:
                current_day = 0
                print()
            current_day += 1

    elif week_day == 5:
        print (" "*11 , end = " ")
        for i in range (1, number_of_days + 1 ):
            if i < 10:
                print ("", i, end = " ")
            else:
                print (i ,  end = " ")
            if current_day == 7 and i != number_of_days:
                current_day = 0
                print()
            current_day += 1

    elif week_day == 6:
        print (" "*14 , end = " " )
        for i in range (1, number_of_days + 1 ):
            if i < 10:
                print ("", i, end = " ")
            else:
                print (i ,  end = " ")
            if current_day == 7 and i != number_of_days:
                current_day = 0
                print()
            current_day += 1

    elif week_day == 7:
        print (" "*17 , end = " " )
        for i in range (1, number_of_days + 1 ):
            if i < 10:
                print ("", i, end = " ")
            else:
                print (i ,  end = " ")
            if current_day == 7 and i != number_of_days:
                current_day = 0
                print()
            current_day += 1
    print ()

def main ():
    week_day, number_of_days = receive_info()
    month_print(week_day, number_of_days) 


if __name__ == "__main__":
    main()

        
