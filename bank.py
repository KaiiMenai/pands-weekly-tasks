# bank.py
# Week 2 task
# author: Kyra Menai Hamilton

# Week 2 task brief - The program should:
#Prompt the user and read in two money amounts (in cent).
#Add the two amounts
#Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
#$ python bank.py
#Enter amount1(in cent): 65
#Enter amount2(in cent): 180
#The sum of these is €2.45

# Process:
# Greeting and ask for input in cents from person inputting.
# Using input from extra reading as a guide: https://github.com/KaiiMenai/pands-mywork/blob/12940891d05aaf77403654a383bcd57e7e86c184/week02/money.py
# Guidance from the web was used for the convert to cent formula formatting.

print("Hello," + "\tPlease enter the following amounts in cents.")
x = input("Enter amount 1: ")
y = input("Enter amount 2: ")
sum = int(x) + int(y)
def converttoeuro(sum):
    return '€{:,.2f}'.format(sum/100)

txt = f"The sum of these is {converttoeuro(sum)}."
print(txt)

# When an input is given of the values listed in the brief the outcome is as follows:
# Hello,  Please enter the following amounts in cents.
# Enter amount 1: 65
# Enter amount 2: 180
# The sum of these is €2.45.

# References:
# My own Ppands-my work repository https://github.com/KaiiMenai/pands-mywork/blob/12940891d05aaf77403654a383bcd57e7e86c184/week02/money.py
# Answer by "Elegent" on stackoverflow (22/11/2015) https://stackoverflow.com/questions/33861401/convert-cents-to-euro
# Further reading worksheet https://www.w3schools.com/python/python_string_formatting.asp