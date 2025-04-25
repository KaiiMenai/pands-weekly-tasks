# Programming and Scripting - Weekly Tasks

Structure of each output
Python Program name: TITLE
Brief Task Description: DESCRIPTION
Example code: If short enough, if not, only packages will be shown.

## Week 1 - helloworld.py

Python Program name: helloworld.py
Brief Task Description: Commit and push a file to the weekly tasks repository called helloworld.py This file should contain a python program that displays Hello World! when it is run.
Example code:
print ('Hello World!')

## Week 2 - bank.py

Python Program name: bank.py
Brief Task Description: The program should:
    - Prompt the user and read in two money amounts (in cent).
    - add the two amounts
    - Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount.
    - $ python bank.py
    - Enter amount1(in cent): 65
    - Enter amount2(in cent): 180
    - The sum of these is €2.45

Example code:
```
print("Hello," + "\tPlease enter the following amounts in cents.")
x = input("Enter amount 1: ")
y = input("Enter amount 2: ")
sum = int(x) + int(y)
def converttoeuro(sum):
    return '€{:,.2f}'.format(sum/100)

txt = f"The sum of these is {converttoeuro(sum)}."
print(txt)
```

## Week 3 - accounts.py

Python Program name: accounts.py
Brief Task Description: The program should:
    - Prompt the user for a 10 character account number.
    - Output the account number with only the last 4 digits shown. For security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).
    - $ python pandsaccount.py
    - Please enter your account number: 1234567890
    - The last 4 digits of your account number are 7890
Extra: Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)
Example code:
```
print("Hello," + "\tPlease enter your 10 digit account number.")
number = input("Enter your account number: ")
while len(number) != 10:
    number = input("That was not a 10 digit number. Please enter your 10 digit account number: ") # I modified the program so that if a number that wasn't 10 digits was entered, the user would be prompted to enter a 10 digit number.

def accountnumber(number):
    return number[-4:]               # This will take the last 4 digits of the account number.

firstsix = 'X' * 6 + number[6:]

print(f"The last 4 digits of your account number are {accountnumber(number)}.")
print(f"Thank you account: {firstsix}." )
```

Extra:
```
print("Hello," + "\tPlease enter your account number.")
second = input("Enter your account number: ")

def accountnumber(second):
    return second[-4:]

allbarfour = 'X' * (len(second) - 4) + second[-4:]      # Replace all characters except the last 4 with 'X's

print(f"The last 4 digits of your account number are {accountnumber(second)}.")
print(f"Thank you account: {allbarfour}.")
```

## Week 4 - collatz.py

Python Program name: collatz.py
Brief Task Description: The program should:
    - Ask the user to input a positive integer.
    - Will output successive values following the calculation method outlined.
    - At each step, it will calculate the next value by taking the current value and:
            - If EVEN, divide by two.
            - If ODD, multiply by three and then add one.
    - The program will end if/when the current value is one.
Example code:
```
while True:
    number = int(input("Enter a positive integer: "))
    print(number)
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        print(number)
```

## Week 5 - weekday.py

Python Program name: weekday.py
Brief Task Description: # Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py). You will need to search the web to find how you work out what day it is. There is no user input.
Packages:
```
import datetime
```

Example code:
```
today = datetime.datetime.today()

if today.weekday() == 4:
    print("Yes, unfortunately today is a weekday.")
elif today.weekday() == 5 or today.weekday() == 6:
    print("It is the weekend, yay!")
else:
    days_to_weekend = 4 - today.weekday()
    print(f"{days_to_weekend} days until the weekend.")
```

## Week 6 - squareroot.py

Python Program name: squareroot.py
Brief Task Description: DESCRIPTION
Example code:
```

```

## Week 7 - numberofes.py

Python Program name: numberofes.py
Brief Task Description: DESCRIPTION
Example code:
```

```

## Week 8 - plottask.py

Python Program name: plottask.py
Brief Task Description: DESCRIPTION
Example code:
```

```