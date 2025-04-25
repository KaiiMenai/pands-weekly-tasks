# accounts.py
# Week 3 task
# This program will read in a 10 character account number and will output the account numberwith only the last 4 digits shown.
# author: Kyra Menai Hamilton

# Weekly Task 03 Brief - The program should:
    # Prompt the user for a 10 character account number.
    # Output the account number with only the last 4 digits shown. For security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).
    # $ python pandsaccount.py
    # Please enter your account number: 1234567890
    # The last 4 digits of your account number are 7890
# Extra: Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)

# Process:
    # Ask user to input account number.
    # Use the slice function to take the last 4 digits of the account number.
    # Print the last 4 digits of the account number.

print("Hello," + "\tPlease enter your 10 digit account number.")
number = input("Enter your account number: ")
while len(number) != 10:
    number = input("That was not a 10 digit number. Please enter your 10 digit account number: ") # I modified the program so that if a number that wasn't 10 digits was entered, the user would be prompted to enter a 10 digit number.

def accountnumber(number):
    return number[-4:]               # This will take the last 4 digits of the account number.

# firstsix = number.replace(number[0:6], "XXXXXX")
# Instead of typing individual X's for each of the characters to be replaced. I need to modify the program to read the number and give the output of characters 1 to 6 as X's. That is replace the first 6 characters with 'X's

firstsix = 'X' * 6 + number[6:]

print(f"The last 4 digits of your account number are {accountnumber(number)}.")
print(f"Thank you account: {firstsix}." )

# Output:
    # Hello,  Please enter your 10 digit account number.
    # Enter your account number: 1234
    # That was not a 10 digit number. Please enter your 10 digit account number: 1234567890
    # The last 4 digits of your account number are 7890.
    # Thank you account: XXXXXX7890.

# This Output is based on a number of assumptions: 
    # The user will input a: 
        # number.
        # no spaces.
        # no special characters.
        # no letters.
        # no symbols.


# Extra
    # Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)

# Process:
# The same, but modify for any account length/number of digits.
# Ask user to input account number.
# Use the slice function to take the last 4 digits of the account number.
# Print the last 4 digits of the account number.

# In order to modify this for any length of input, the length input will need to be used. So could use len(in)-4.

print("Hello," + "\tPlease enter your account number.")
second = input("Enter your account number: ")

def accountnumber(second):
    return second[-4:]          

allbarfour = 'X' * (len(second) - 4) + second[-4:]      # Replace all characters except the last 4 with 'X's

print(f"The last 4 digits of your account number are {accountnumber(second)}.")
print(f"Thank you account: {allbarfour}.")

# Output:
    # Hello,  Please enter your account number.
    # Enter your account number: 112233445566
    # The last 4 digits of your account number are 5566.
    # Thank you account: XXXXXXXX5566.

# References:   
    # My own pands-my work repository https://github.com/KaiiMenai/pands-mywork/blob/12940891d05aaf77403654a383bcd57e7e86c184/week02/money.py
    # Weekly Task 2 bank.py
    # Extra reading worksheet https://realpython.com/python-string-formatting/#interpolating-and-formatting-strings-in-python
    # Extra reading https://www.w3schools.com/python/ref_func_slice.asp
    # To limit input to 10 digits https://stackoverflow.com/questions/19970569/how-to-limit-the-input-of-a-user-to-only-10-digits
    # Used length of input to limit the number of digits but also to replace all but the last 4 digits with X's. https://www.w3schools.com/python/ref_func_len.asp
    # I asked copilot to expllain how I would modify the output characters 1 to 6/all bar last 4 as X's. https://copilot.github.com/
    # The extra reading I did for this task was to understand the slice function in Python. https://www.w3schools.com/python/ref_func_slice.asp

# End