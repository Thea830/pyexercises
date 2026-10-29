"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: my list from exercise 4.0: [4, 5, 6, 7, 8, 9]
# 2. Process: go through each number, count its position, and compute its square
# 3. Out: one line per number with its position, the number, and its square (6 numbers, so exactly 6 lines)
# 4. What I compute for each item, and why it is worth showing: I compute the square of each number (number * number). The reader learns how fast the squares grow, even when the numbers grow slowly.


# Your code below
list = [4, 5, 6, 7, 8, 9]

print("List of numbers and their squares:")

position = 1
for i in list:
    square = i ** 2
    print("Number: ", i,"Position: ", position, "Square: ", square)
    position = position + 1
