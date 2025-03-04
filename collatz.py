# collatz.py
# Week 4 task
# This program will asks the user to input any positive integer and outputs the successive values following a calculation, until the current value is one.
# author: Kyra Menai Hamilton

# Weekly Task 04 Brief - The program should:
    # Ask the user to input a positive integer.
    # Will output successive values following the calculation method outlined.
    # At each step, it will calculate the next value by taking the current value and:
            # If EVEN, divide by two.
            # If ODD, multiply by three and then add one.
    # The program will end if/when the current value is one.

while True:
    number = int(input("Enter a positive integer: "))
    print(number)
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        print(number)

# Output: 
    # Enter a positive integer: 10
    # 10
    # 5
    # 16
    # 8
    # 4
    # 2
    # 1

# The code asks for a positive integer.
# Using example in userinloop.py (line 11) can see how to note a termination condition with "!=".
# So here I've stated that if the number becomes 1, then that is the point at which this loop will end.
# Using example from iseven.py and iseven2.py can see how to check if a number is EVEN. 
# So here the "if" statement refers to the EVEN number, whilst the "else" refers to the ODD.
# Thus (EVEN/2), and (ODD*3)+1.

# References:
# Collatz Conjecture - https://www.youtube.com/watch?v=094y1Z2wpJg&t=1s
# whileloop.py - https://github.com/KaiiMenai/pands-mywork/blob/main/week04/whileloop.py
# userinloop.py - https://github.com/KaiiMenai/pands-mywork/blob/main/week04/userinloop.py
# iseven.py - https://github.com/KaiiMenai/pands-mywork/blob/main/week04/iseven.py
# iseven2.py - https://github.com/KaiiMenai/pands-mywork/blob/main/week04/iseven2.py

# END
