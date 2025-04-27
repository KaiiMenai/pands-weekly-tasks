# Programming and Scripting - Weekly Tasks

author: Kyra Menai Hamilton

Contained within this repository (pands-weekly-tasks) are programs made for part of the assessment for the Program and Scripting Module (2025 January start).

There are eight programs, these are in order of the weekly tasks:

1. helloworld.py
2. bank.py
3. accounts.py
4. collatz.py
5. weekday.py
6. squareroot.py
7. numberofes.py
8. plottask.py

There are three PNG files, these are figures for the task during week 8.

A copy of the weekly tasks PDF file is contained to ensure clarity and adherence to the course requirements.

References are included at the bottom of the README.md with relevant task and task program noted.

## Week 1 - helloworld.py

Python Program name: helloworld.py

**Task Description**

- Commit and push a file to the weekly tasks repository called helloworld.py 
- This file should contain a python program that displays Hello World! when it is run.

Example code:

```ruby
print ('Hello World!')
```

## Week 2 - bank.py

Python Program name: bank.py

**Task Description**

The program should:

- Prompt the user and read in two money amounts (in cent).
- add the two amounts
- Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount.

Example code:
```ruby
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

**Task Description**

The program should:

- Prompt the user for a 10 character account number.
- Output the account number with only the last 4 digits shown. For security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).

Extra: Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)

Example code:
```ruby
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
```ruby
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

**Task Description**

The program should:

- Ask the user to input a positive integer.
- Will output successive values following the calculation method outlined.
- At each step, it will calculate the next value by taking the current value and:
  - If EVEN, divide by two.
  - If ODD, multiply by three and then add one.
- The program will end if/when the current value is one.

Example code:
```ruby
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

**Task Description**

The program should:

- Output whether or not today is a weekday.

Packages:
```
import datetime
```

Example code:
```ruby
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

**Task Description**

The program should:

- Take a positive floating-point number as input and outputs an approximation of its square root.
- The function that does this should be called <tt>sqrt</tt>.

Example code:
```ruby
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

## Week 7 - numberofes.py

Python Program name: numberofes.py

**Task Description**

The program should:

- Read in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.
- The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.
- Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.

Packages:
```
import urllib.request 
```

Example code:
```ruby
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

## Week 8 - plottask.py

Python Program name: plottask.py

**Task Description**

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
```ruby
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

## References

ChatGPT (n.d.) *Reference assistance and formatting support*. OpenAI. Available at: https://openai.com/chatgpt (*Week 7, numberofes.py*)

Clontz, S. (n.d.) *mobydick.txt (gist repository overview)*. Available at: https://gist.github.com/StevenClontz/4445774#file-mobydick-txt (*Week 7, numberofes.py*).

Clontz, S. (n.d.) *mobydick.txt – Moby Dick full text (Herman Melville)*. Available at: https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt (*Week 7, numberofes.py*).

Elegent (2015) ‘Convert cents to euro’. *Stack Overflow*. Available at: https://stackoverflow.com/questions/33861401/convert-cents-to-euro (*Week 2, bank.py*).

GeeksforGeeks (n.d.) *Find root of a number using Newton’s method*. Available at: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/ (*Week 6, squareroot.py*).

GeeksforGeeks (n.d.) *Program for Newton-Raphson Method*. Available at: https://www.geeksforgeeks.org/program-for-newton-raphson-method/ (*Week 6, squareroot.py*).

GeeksforGeeks (n.d.) *Square root of a perfect square*. Available at: https://www.geeksforgeeks.org/square-root-of-a-perfect-square/ (*Week 6, squareroot.py*).

GitHub (n.d.) *Creating and Highlighting Code Blocks*. Available at: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks (*Markdown Syntax Highlighting*).

GitHub Copilot (n.d.) *GitHub Copilot*. Available at: https://copilot.github.com/ (*Week 3, accounts.py*).

KaiiMenai (n.d.) *loopyloop.py*. GitHub. Available at: https://github.com/KaiiMenai/pands-mywork/blob/main/week04/loopyloop.py (*Week 7, numberofes.py*)

Killbourne, A.M. and Williams, M.V. (2003) ‘Understanding the literature on cultural competence and health care disparities’, *Public Health Reports*, 118(4), pp. 293–302. Available at: https://pmc.ncbi.nlm.nih.gov/articles/PMC1480066/ (*Week 7, numberofes.py*).

Matplotlib (2019) *matplotlib.pyplot.savefig — Save a figure*. Available at: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.savefig.html (*Week 8, plottask.py*).

Matplotlib (n.d.) *matplotlib.colors — Colors in Matplotlib*. Available at: https://matplotlib.org/stable/tutorials/colors/colors.html (*Week 8, plottask.py*).

Matplotlib (n.d.) *matplotlib.legend — Matplotlib Legend Guide*. Available at: https://matplotlib.org/stable/tutorials/intermediate/legend_guide.html (*Week 8, plottask.py*).

Matplotlib (n.d.) *matplotlib.pyplot — Matplotlib’s Pyplot*. Available at: https://matplotlib.org/stable/tutorials/introductory/pyplot.html (*Week 8, plottask.py*).

Matplotlib (n.d.) *matplotlib.pyplot.hist — Plot a histogram*. Available at: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html (*Week 8, plottask.py*).

Matplotlib (n.d.) *matplotlib.pyplot.plot — Plot lines and/or markers to the axes*. Available at: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html (*Week 8, plottask.py*).

Matplotlib (n.d.) *matplotlib.pyplot.savefig — Save a figure*. Available at: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html (*Week 8, plottask.py*).

Menai, K. (n.d.) *accounts.py – pands-weekly-tasks repository*. Available at: https://github.com/KaiiMenai/pands-weekly-tasks/blob/main/accounts.py (*Week 7, numberofes.py*).

Menai, K. (n.d.) *collatz.py – pands-weekly-tasks repository*. Available at: https://github.com/KaiiMenai/pands-weekly-tasks/blob/main/collatz.py (*Week 7, numberofes.py*).

Menai, K. (n.d.) *grade2.py – Basic structure of if/else loop*. Available at: https://github.com/KaiiMenai/pands-mywork/blob/main/week04/grade2.py (*Week 6, squareroot.py*).

Menai, K. (n.d.) *iseven.py – pands-mywork repository*. Available at: https://github.com/KaiiMenai/pands-mywork/blob/main/week04/iseven.py (*Week 4, collatz.py*).

Menai, K. (n.d.) *iseven2.py – pands-mywork repository*. Available at: https://github.com/KaiiMenai/pands-mywork/blob/main/week04/iseven2.py (*Week 4, collatz.py*).

Menai, K. (n.d.) *loopyloop.py - while loop function*. Available at: https://github.com/KaiiMenai/pands-mywork/blob/main/week04/loopyloop.py (*Week 6, squareroot.py*).

Menai, K. (n.d.) *stringformat.py – Format output to 2 decimal places*. Available at: https://github.com/KaiiMenai/pands-mywork/blob/main/week03/stringformat.py (*Week 6, squareroot.py*).

Menai, K. (n.d.) *userinloop.py – pands-mywork repository*. Available at: https://github.com/KaiiMenai/pands-mywork/blob/main/week04/userinloop.py (*Week 4, collatz.py*).

Menai, K. (n.d.) *whileloop.py – pands-mywork repository*. Available at: https://github.com/KaiiMenai/pands-mywork/blob/main/week04/whileloop.py (*Week 4, collatz.py*).

nkmk (n.d.) *Counting characters in a string with str.count() method*. Available at: https://note.nkmk.me/en/python-str-count/ (*Week 7, numberofes.py*)

NumPy (n.d.) *numpy.linspace — Return evenly spaced numbers over a specified interval*. Available at: https://numpy.org/doc/stable/reference/generated/numpy.linspace.html (*Week 8, plottask.py*).

NumPy (n.d.) *numpy.ndarray — N-dimensional array object*. Available at: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html (*Week 8, plottask.py*).

NumPy (n.d.) *numpy.random.normal — Normal (Gaussian) Distributions*. Available at: https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html (*Week 8, plottask.py*).

NumPy (n.d.) *numpy.round_ — Round an array to the given number of decimals*. Available at: https://numpy.org/doc/stable/reference/generated/numpy.round_.html (*Week 8, plottask.py*).

Perplexity.ai (n.d.) *Used for checking spelling in code and asking coding-related queries*. Available at: https://www.perplexity.ai (*Week 7, numberofes.py*)

Programiz (n.d.) *Python datetime: Manipulate Dates and Times in Python*. Available at: https://www.programiz.com/python-programming/datetime/current-datetime (*Week 5, weekday.py*).

Programiz (n.d.) *Python exception handling with try-except blocks*. Available at: https://www.programiz.com/python-programming/exception-handling (*Week 7, numberofes.py*)

Python Software Foundation (n.d.) *Built-in Exceptions*. Available at: https://docs.python.org/3/library/exceptions.html (*Week 7, numberofes.py*).

Python Software Foundation (n.d.) *Downloading files with urllib.request.urlretrieve*. Available at: https://docs.python.org/3/library/urllib.request.html (*Week 7, numberofes.py*)

Python Software Foundation (n.d.) *Errors and Exceptions – Python 3 Tutorial*. Available at: https://docs.python.org/3/tutorial/errors.html (*Week 7, numberofes.py*).

Python Software Foundation (n.d.) *urllib.request — Extensible library for opening URLs*. Available at: https://docs.python.org/3/library/urllib.request.html (*Week 7, numberofes.py*).

Read the Docs (n.d.) *Fetching URLs and using urllib.request module*. Available at: https://python.readthedocs.io/fr/stable/howto/urllib2.html (*Week 7, numberofes.py*)

Real Python (n.d.) *Python String Formatting*. Available at: https://realpython.com/python-string-formatting/#interpolating-and-formatting-strings-in-python (*Week 3, accounts.py*).

Real Python (n.d.) *Python While Loops – A Comprehensive Guide*. Available at: https://realpython.com/python-while-loop/ (*Week 6, squareroot.py*).

Real Python (n.d.) *Understanding Python Iterators: A Guide*. Available at: https://realpython.com/python-iterators/ (*Week 6, squareroot.py*).

Real Python (n.d.) *Using Assignment Expressions in Python*. Available at: https://realpython.com/python-assignment-expressions/ (*Week 6, squareroot.py*).

Scivision (n.d.) *Comparison of urllib.request.urlretrieve and requests including timeout handling*. Available at: https://www.scivision.dev/python-switch-urlretrieve-requests-timeout/ (*Week 7, numberofes.py*)

Stack Overflow (2011) *matplotlib savefig plots different from show*. Available at: https://stackoverflow.com/questions/7906365/matplotlib-savefig-plots-different-from-show (*Week 8, plottask.py*).

Stack Overflow (2013) *How to limit the input of a user to only 10 digits*. Available at: https://stackoverflow.com/questions/19970569/how-to-limit-the-input-of-a-user-to-only-10-digits (*Week 3, accounts.py*).

Stack Overflow (n.d.) *Counting occurrences of a character in a string on Stack Overflow*. Available at: https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string (*Week 7, numberofes.py*)

Stack Overflow (n.d.) *Discussion on urllib.request.urlretrieve vs urlopen on Stack Overflow*. Available at: https://stackoverflow.com/questions/56915019/should-i-switch-from-urllib-request-urlretrieve-to-urllib-request-urlopen (*Week 7, numberofes.py*)

Veritasium (2021) ‘The Simplest Math Problem No One Can Solve - Collatz Conjecture’, *YouTube*. Available at: https://www.youtube.com/watch?v=094y1Z2wpJg&t=1s (*Week 4, collatz.py*).

W3Schools (n.d.) *Python String Formatting*. Available at: https://www.w3schools.com/python/python_string_formatting.asp (*Week 2, bank.py*).

W3Schools (n.d.) *Python datetime Module*. Available at: https://www.w3schools.com/python/python_datetime.asp (*Week 5, weekday.py*).

W3Schools (n.d.) *Python ref_func_len() Method*. Available at: https://www.w3schools.com/python/ref_func_len.asp (*Week 3, accounts.py*).

W3Schools (n.d.) *Python ref_func_slice() Method*. Available at: https://www.w3schools.com/python/ref_func_slice.asp (*Week 3, accounts.py*).

W3Schools (n.d.) *Python try-except explanation and examples on W3Schools*. Available at: https://www.w3schools.com/python/python_try_except.asp (*Week 7, numberofes.py*)

Walsh, M. (n.d.) *File reading with encoding in Python (open() function)*. Available at: https://melaniewalsh.github.io/Intro-Cultural-Analytics/02-Python/07-Files-Character-Encoding.html (*Week 7, numberofes.py*)