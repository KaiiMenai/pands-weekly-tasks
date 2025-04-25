# Programming and Scripting - Weekly Tasks

## Week 1 - helloworld.py

Python Program name: helloworld.py

Task Description

- Commit and push a file to the weekly tasks repository called helloworld.py 
- This file should contain a python program that displays Hello World! when it is run.

Example code:

```
print ('Hello World!')
```

References:
Datacamp (n.d.) Python Hello World: A Beginner’s Guide to Programming. Available at: https://www.datacamp.com/tutorial/python-hello-world-a-beginners-guide-to-programming (Accessed: 25 April 2025).

## Week 2 - bank.py

Python Program name: bank.py

Task Description

The program should:

- Prompt the user and read in two money amounts (in cent).
- add the two amounts
- Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount.

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

References:


## Week 3 - accounts.py

Python Program name: accounts.py

Task Description

The program should:

- Prompt the user for a 10 character account number.
- Output the account number with only the last 4 digits shown. For security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).

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

References:


## Week 4 - collatz.py

Python Program name: collatz.py

Task Description

The program should:

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

References:


## Week 5 - weekday.py

Python Program name: weekday.py

Task Description

- Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py).
- You will need to search the web to find how you work out what day it is. 
- There is no user input.

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

References:


## Week 6 - squareroot.py

Python Program name: squareroot.py

Task Description

- Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
- You should create a function called <tt>sqrt</tt> that does this.
- I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
- This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots. 
- This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.

Example code:
```
to_root = float(input("Please enter a positive number: "))
# print(to_root) # To check that the input is being stored correctly.

if to_root <0:                                                          # The program will not work for negative numbers.
    print("Please enter a positive number. ")
else:
    approx_root = to_root/2                                             # Initial guess will be half of the number.
    while abs(to_root - approx_root**2) > 0.01:                         # The loop will run until the difference between the number and the square root of the approximation is less than 0.01.
        approx_root = (approx_root + to_root/approx_root)/2             # The approximation will be updated using the formula for Newton's method.
    print(f"The square root of {to_root} is approx. {approx_root:.2f}.")    # The approx. square root will be printed out.
```

References:


## Week 7 - numberofes.py

Python Program name: numberofes.py

Task Description

- Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.
- The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.
- Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.

Packages:
```
import urllib.request 
```

Example code:
```
# Function to count occurrences of the letter 'e' in a file from a URL.
def count_letter_e_in_url(url):
    try:
        # Open the URL and read the content
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')  # Decode the content to a string
            
            # Count occurrences of 'e' (lowercase) and 'E' (uppercase)
            lowercase_e_count = content.count('e')
            uppercase_e_count = content.count('E')
            
            # Calculate the total count
            total_count = lowercase_e_count + uppercase_e_count
            
            return lowercase_e_count, uppercase_e_count, total_count
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0, 0

url = "https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt" # URL of the text file

# Use the function to get the counts.
lowercase_count, uppercase_count, total_count = count_letter_e_in_url(url)

# Print the results - I wanted to make sure that I checked both the lowercase and uppercase 'e' characters.
if total_count > 0:
    print(f"The letter 'e' appears {lowercase_count} times as lowercase and {uppercase_count} times as uppercase.")
    print(f"Total occurrences of the letter 'e' (both uppercase and lowercase): {total_count}.")
else:
    print("Failed to count the occurrences of 'e'.")
```

References:


## Week 8 - plottask.py

Python Program name: plottask.py

Task Description

Write a program called plottask.py that displays:

- a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
- and a plot of the function  h(x)=x3 in the range 0 to 10, 
on the one set of axes.

Packages:
```
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
```

Example code:
```
# First create the values for the normal distribution. Requirements are 1000 values, mean of 5 and standard deviation of 2.
mean = 5
std_dev = 2
rdm_values = np.random.normal(mean, std_dev, 1000)

# The initial values had a LOT of decimal places, so I used the round() function to round the values to 2 decimal places.
values = np.round(rdm_values, 2)

# Check that is works by printing the values as a list [].
# print(values)

# Now to plot the histogram of the normal distribution. Making sure to include labelling and legends.add_subplot(111) is used to create a single plot.

plt.hist(values, bins=30, color='c', edgecolor='black', alpha=0.7, label='Normal Distribution Values (mean = 5, std = 2)')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of a Normal Distribution for 1000 random values \n(Mean = 5, Standard Deviation = 2)')
plt.legend(title='Legend')
# Save the figure as a PNG file
plt.savefig('week8task_figure_1_normaldist1000.png')
plt.show()

# Plot output shown in: week8task_figure_1_normaldist1000.png for histogram of normal distribution of 1000 values.

# PART 2

# Now to plot the function h(x)=x^3 in the range 0 to 10.
# Create the range of values from 0 to 10.
x = np.linspace(0, 10, 100)
y = x**3

# Plot the function h(x)=x^3 in the range 0 to 10.
# This will make a line plot of the function h(x)=x^3 in the range 0 to 10.
plt.plot(x, y, color='m', label='h(x)=x^3')
plt.xlabel('x')
plt.ylabel('h(x)')
plt.title('Plot of the function h(x)=x^3 in the range 0 to 10.')
plt.legend(title='Legend')
plt.savefig('week8task_figure_2_h(x)plot.png')
plt.show()

# Plot output shown in: week8task_figure_2_h(x)plot.png for plot of the function h(x)=x^3 in the range 0 to 10.

# Combined plot of both the histogram and the function h(x)=x^3 in the range 0 to 10. 
# This was made using extracts from the code above, and combining them into one plot.
# Values for the Normal Dist.
mean = 5
std_dev = 2
rdm_values = np.random.normal(mean, std_dev, 1000)
values = np.round(rdm_values, 2) 

# Range of values for the h(x) = x^3 function.
x = np.linspace(0, 10, 100)
y = x**3

# Combined plot - state size of figure.
plt.figure(figsize=(10, 6))

# Plot the histogram of the Normal Dist.
plt.hist(values, bins=30, color='c', edgecolor='black', alpha=0.7, label='Normal Distribution Values (mean = 5, std = 2)')

# Plot the function h(x)=x^3
plt.plot(x, y, color='m', label='h(x)=x^3')

# Add the labels, title, and legend.
plt.xlabel('Values / x')
plt.ylabel('Frequency / h(x)')
plt.title('Combined Plot: Histogram of Normal Distribution and h(x)=x^3')
plt.legend(title='Legend')

# Save the figure as a PNG file and print it out.
plt.savefig('week8task_figure_3_combined_plot.png')
plt.show()
```

References:

