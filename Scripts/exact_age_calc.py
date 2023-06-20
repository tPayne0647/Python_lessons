# Exact age calculator

import re
import datetime

def calculate_age():
    name_pattern = r'^[a-zA-Z]+$'
    date_pattern = r'^\d{2}$'
    time_pattern = r'^\d{2}:\d{2}(am|pm)$'

    name = input("What is your name?: ")
    while not re.match(name_pattern, name):
        print("Invalid name format. Please enter only letters.")
        name = input("What is your name?: ")

    month = input("What month were you born in? (2-digit number): ")
    while not re.match(date_pattern, month) or int(month) > 12:
        print("Invalid month format. Please enter a valid 2-digit number. (1-12)")
        month = input("What month were you born in? (2-digit number): ")

    day = input("What day were you born on? (2-digit number): ")
    while not re.match(date_pattern, day) or int(day) > 31:
        print("Invalid day format. Please enter a valid 2-digit number. (1-31)")
        day = input("What day were you born on? (2-digit number): ")

    year = input("What year were you born? (4-digit number): ")
    while not re.match(r'^\d{4}$', year) or int(year) < 1900 or int(year) > datetime.datetime.now().year:
        print("Invalid year format. Please enter a valid 4-digit number between 1900 and the current year.")
        year = input("What year were you born? (4-digit number): ")

    ask_time = input("Do you know what time you were born? (yes/no): ")
    
    if ask_time.lower() == "yes":
        time = input("What time were you born? (XX:XXam/pm): ")
        while not re.match(time_pattern, time):
            print("Invalid time format. Please use the format XX:XXam/pm.")
            time = input("What time were you born? (XX:XXam/pm): ")
    else:
        time = "00:00am"

    birth_date_str = f"{year}-{month}-{day} {time}"
    birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d %I:%M%p")
    current_date = datetime.datetime.now()

    age = current_date - birth_date

    years = age.days // 365
    days_remaining = age.days % 365

    # Adjusting for leap years
    leap_days = sum(1 for y in range(int(year), current_date.year + 1) if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0)
    if current_date.month < int(month) or (current_date.month == int(month) and current_date.day < int(day)):
        leap_days -= 1

    days_remaining -= leap_days

    hours, remainder = divmod(age.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    print(f"Hello, {name}!")
    if years > 0:
        print(f"You are {years} years, {days_remaining} days, {hours} hours, and {minutes} minutes old.")
    else:
        print(f"You are {days_remaining} days, {hours} hours, and {minutes} minutes old.")

calculate_age()