# ADT to represent a time

def create_time(hour, minute):
    """ returns a time given hour and minute"""
    return hour*60 + minute

def get_hour(time):
    """ Gets hour from time """
    return time // 60

def get_minute(time):
    """ Gets minute from time """
    return time % 60

def split(time):
    """ returns a tuple of (hour, minute) from time """
    return (get_hour(time), get_minute(time))

def to_string(time):
    """ returns a string representation of a time in format HH:MM """
    return '{:02d}:{:02d}'.format(*split(time))

def less(t1, t2):
    """ returns true if time t1 is less than t2 """
    return t1 < t2

def equal(t1, t2):
    """ returns true if times t1 and t2 are equal """
    return t1 == t2

