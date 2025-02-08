# Week 2 task
# The program should:

#Prompt the user and read in two money amounts (in cent)
#Add the two amounts
#Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
#$ python bank.py
#Enter amount1(in cent): 65
#Enter amount2(in cent): 180
#The sum of these is €2.45

print("Hello," + "\tPlease enter the following amounts in cents.")
x = input("Enter amount 1: ")
y = input("Enter amount 2: ")
sum = int(x) + int(y)
def convertToCent(sum):
    return '€{:,.2f}'.format(sum/100)

txt = f"The sum of these is {convertToCent(sum)}."
print(txt)