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
print("Hello," + "\tPlease enter the following amounts in cents.")
x = input("Enter amount 1: ")
y = input("Enter amount 2: ")
sum = int(x) + int(y)
def converttoeuro(sum):
    return '€{:,.2f}'.format(sum/100)

txt = f"The sum of these is {converttoeuro(sum)}."
print(txt)

## Week 3

Python Program name: TITLE
Brief Task Description: The program should:
    - Prompt the user for a 10 character account number.
    - Output the account number with only the last 4 digits shown. For security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).
    - $ python pandsaccount.py
    - Please enter your account number: 1234567890
    - The last 4 digits of your account number are 7890
Extra: Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)
Example code:

## Week 4

Python Program name: TITLE
Brief Task Description: DESCRIPTION
Example code:

## Week 5

Python Program name: TITLE
Brief Task Description: DESCRIPTION
Example code:

## Week 6

Python Program name: TITLE
Brief Task Description: DESCRIPTION
Example code:

## Week 7

Python Program name: TITLE
Brief Task Description: DESCRIPTION
Example code:

## Week 8

Python Program name: TITLE
Brief Task Description: DESCRIPTION
Example code:
