# squareroot.py
# Week 6 task
# This program takes a positive floating-point number as input and outputs an approximation of its square root.
# author: Kyra Menai Hamilton

# This will be done without the math module or any other inbuilt function in python (for the purpose of the task).

to_root = float(input("Please enter a positive number: "))
# print(to_root) # To check that the input is being stored correctly.

if to_root <0:                                                          # The program will not work for negative numbers.
    print("Please enter a positive number. ")
else:
    approx_root = to_root/2                                             # Initial guess will be half of the number.
    while abs(to_root - approx_root**2) > 0.01:                         # The loop will run until the difference between the number and the square of the approximation is less than 0.01.
        approx_root = (approx_root + to_root/approx_root)/2             # The approximation will be updated using the formula for Newton's method.
    print(f"The square root of {to_root} is approx. {approx_root:.2f}.")    # The approximation will be printed out.

# Output: 
# Please enter a positive number: 14.5
# The square root of 14.5 is approx. 3.81


# References: 

# Basic structure of if else loop: https://github.com/KaiiMenai/pands-mywork/blob/main/week04/grade2.py
# To get 2 dp answer: https://github.com/KaiiMenai/pands-mywork/blob/main/week03/stringformat.py
# https://realpython.com/python-while-loop/
# https://realpython.com/python-iterators/
# https://realpython.com/python-assignment-expressions/
# https://en.wikipedia.org/wiki/Newton%27s_method
# https://www.geeksforgeeks.org/square-root-of-a-perfect-square/
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
# https://www.geeksforgeeks.org/program-for-newton-raphson-method/
# https://flexiple.com/python/newton-raphson-method-python

# END