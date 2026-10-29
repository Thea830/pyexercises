"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: user input of yes or no 
# 2. Process: asking the user for input until they provide a valid answer, and counting the number of attempts
# 3. Out: displaying the number of attempts and whether the user chose to continue or not
# 4. My stop condition, my attempt limit, my summary: the stop condition is when the user inputs "yes" or "no", the maximum number of attempts is 5, and the summary contains the number of attempts and whether the user chose to continue or not.


# Your code below
i = 0 
while i < 5:
    print("attempt number: ", i + 1)
    i = i + 1
    
while True:
    answer = input("do you want to continue? (yes/no): ")
    if answer.strip().lower() == "yes":
        print("you chose to continue.")
        break
    elif answer.strip().lower() == "no":
        print("you chose not to continue.")
        break
    else: 
        print("invalid input. please enter 'yes' or 'no'.")
        break