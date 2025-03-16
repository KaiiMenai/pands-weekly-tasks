# weekday.py
# Week 5 task
# This program will output whether or not today is a weekday.
# author: Kyra Menai Hamilton

# Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)
# You will need to search the web to find how you work out what day it is.
# There is no user input.

import datetime

today = datetime.datetime.today()

if today.weekday() == 4:
    print("Yes, unfortunately today is a weekday.")
elif today.weekday() == 5 or today.weekday() == 6:
    print("It is the weekend, yay!")
else:
    days_to_weekend = 4 - today.weekday()
    print(f"{days_to_weekend} days until the weekend.")

# This code imports the datetime module and retrieves today's date using datetime.datetime.today(). 
# It then checks the day of the week using the today.weekday() method, which returns an integer from 0 (Monday) to 6 (Sunday).
# The program will output whether or not today is a weekday.

# Output
    # It is the weekend, yay! (I ran this on a Sunday).

# References:
# https://docs.python.org/3/library/datetime.html
# https://www.w3schools.com/python/python_datetime.asp
# https://www.programiz.com/python-programming/datetime/current-datetime
# https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python

# END