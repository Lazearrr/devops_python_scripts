import time
import os

def get_current_time():
    current_time = str(time.time())

    sep = '.'
    stripped = current_time.split(sep, 1)[0]
    stripped = stripped + "000"
    return stripped

def calculate_input_epoch():
    days = os.getenv("days")
    days = int(days)
    days_epoch_ms = days * 86400000
    return days_epoch_ms

first = int(get_current_time())
second = int(calculate_input_epoch())

third = first - second
str(third)
print(third.strip())
