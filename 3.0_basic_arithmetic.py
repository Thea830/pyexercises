"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: two numbers
# 2. Process: ask the user for two numbers, then perform addition, subtraction, multiplication, and division on them
# 3. Out: the results of the four operations displayed to the user
# 4. What happens when the second number is zero, and why: i decided to display a message instead of a result when the second number is zero, because division by zero is undefined and it is important to inform the user about that.


# Your code below
number_1 = int(input("enter number 1: "))
number_2 = int(input("enter number 2: "))

print("the number 1 is: ", number_1)
print("the number 2 is: ", number_2)

sum = number_1 + number_2
print("the sum of two numbers is: ", sum)

difference = number_1 - number_2
print("the difference of two numbers is : ", difference)

if number_2 != 0:
    div = number_1 / number_2
    print("the division of two numbers is: ", div)
else:
    print("division by zero is not allowed")
