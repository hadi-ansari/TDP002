from my_time import *

def create_calendar(num):
    calendar = []
    for i in range(num):
        new_lane = {"number": i + 1,"from": None, "until"= None}
        calendar.append(new_lane)
        
    return calendar

def reserve(calendar, num, start, stop):
    for i in calendar:
        if calendar[i]["number"] == num:
            if calendar[i]["from"] == None:
                calendar[i]["from"] = start
                calendar[i]["until"] = stop
                return True
            
            elif less(start, calendar[i]["until"]) or less(calendar[i]["from"], stop)
                return False
            
            else:
                calendar[i]["from"] = start
                calendar[i]["until"] = stop
                return True

    return False
                
                
        
def available(calendar, num, time):
    return 0
def available_lanes(calendar, time):
    return 0



c1 = create_calendar(5)
for i in c1:
    print(i)

reserve(c1, 1, )
