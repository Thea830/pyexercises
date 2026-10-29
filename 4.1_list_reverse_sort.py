"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of numbers
# 2. Process: Reordering the list in different ways
# 3. Out: Four different ordered versions of the list
# 4. My four orders, and which ones modify the original: Biggest to smallest, every other number first, second half first,first number at the end. None modify the original: .sort() is used on a copy, and slicing makes a new list.

# Your code below
my_list = [4, 5, 6, 7, 8, 9]
 
copy = my_list.copy()
copy.sort(reverse=True)
print("Biggest to smallest: ", copy)
 
print("Every other number first:", my_list[::2] + my_list[1::2])
 
print("Second half first: ", my_list[3:] + my_list[:3])
 
print("First number at the end: ", my_list[1:] + my_list[:1])
 
print("Original list: ", my_list)