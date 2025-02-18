# pandsaccount.py
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
    number = input('That was not a 10 digit number. Please enter your 10 digit number. ')

def accountnumber(x):
    return number[-4:]
firstsix = number.replace(number[0:6], "XXXXXX")
print(f"The last 4 digits of your account number are {accountnumber(number)}.")
print(f"Thank you account: {firstsix}." )

# Output:
    # Hello,  Please enter your 10 digit account number.
    # Enter your account number: 1234567890
    # The last 4 digits of your account number are 7890.
    # Thank you account: XXXXXX7890.
# Instead of typing individual X's for each of the characters to be replaced.

# Modifying the [0:6] (this goes forward) to [0:-4] (this goes backward) will go from character 0 to the 4th last character and replace them with X.

# This Output is based on a number of assumptions: 
    # The user will input a: 
        # 10 digit account number.
        # number.
        # no spaces.
        # no special characters.
        # no letters.
        # no symbols.

# The extra reading I did for this task was to understand the slice function in Python. https://www.w3schools.com/python/ref_func_slice.asp

# Extra
    # Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)

# Process:
# The same, but modify for any account length/number of digits.
# Ask user to input account number.
# Use the slice function to take the last 4 digits of the account number.
# Print the last 4 digits of the account number.

# print("Hello," + "\tPlease enter your account number.")
# second = input("Enter your account number: ")

# def accountnumber(x):
#    return second[-4:]      # This will take the last 4 digits of the account number.
# lastfour = second.replace(second[0:-4], "X") # This will replace all digits except the last 4 with X.

# print(f"The last 4 digits of your account number are {accountnumber(second)}.")
# print(f"Thank you account: {lastfour}.")

# References:   
    # My own Ppands-my work repository https://github.com/KaiiMenai/pands-mywork/blob/12940891d05aaf77403654a383bcd57e7e86c184/week02/money.py
    # Weekly Task 2 bank.py
    # Extra reading worksheet https://realpython.com/python-string-formatting/#interpolating-and-formatting-strings-in-python
    # Extra reading https://www.w3schools.com/python/ref_func_slice.asp
    # To limit input to 10 digits https://stackoverflow.com/questions/19970569/how-to-limit-the-input-of-a-user-to-only-10-digits
