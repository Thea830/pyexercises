"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A positive integer entered by the user
# 2. Process: Check if each number from 1 to N is odd or even
# 3. Out: For each number, indicate whether it is odd or even
# 4. What happens on 0, on a negative number, on a very large number:
#    - On 0: Display a message indicating no numbers to check
#    - On a negative number: Display a message asking for a positive number
#    - On a very large number: Display a message asking for a smaller number

# Your code below
n = int(input("Enter a number: "))
 
if n == 0:
    print("There are no numbers from 1 to 0, nothing to show.")
elif n < 0:
    print("Please enter a positive number.")
elif n > 100:
    print("That is too many numbers. Please enter a number up to 100.")
else:
    for number in range(1, n + 1):
        if number % 2 == 0:
            print(number, "is even")
        else:
            print(number, "is odd")