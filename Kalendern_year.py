#! /usr/bin/env python3

import Kalendern
from Kalendern import month_print



def last_day_in_month(start_day, month_days):
    
    current_day = start_day
    for i in range (0 , month_days ):
        if (current_day == 7):
            current_day = 0
        current_day += 1
        
    return current_day;



def main():

    start_day = int(input("Mata in veckodagen:\t"))
    month_of_year = ["Januari", "Februari", "Mars", "April", "Maj", "Juni", "Juli", "Augusti", "September", "Oktober", "November", "December"]

    for i in range (1, 13):
        print()
        print (month_of_year[i-1])
        if i == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            month_print(start_day, 31)
            start_day = last_day_in_month(start_day, 31)
        elif i == 4 or 6 or 9 or 11:
            month_print(start_day, 30)
            start_day = last_day_in_month(start_day, 30)
        else:
            month_print(start_day, 28)
            start_day = last_day_in_month(start_day, 28)


if __name__ == "__main__":
    main()
