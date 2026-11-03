"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of numbers
# 2. Process, function by function: each function does one thing: the first finds the smallest number, the second finds the largest number, and the third calculates the average of the numbers in the list. The fourth function uses the results of the first three functions to determine if the average is exactly in the middle between the smallest and largest numbers.
# # 3. Out: The fourth function returns a boolean value indicating whether the average is in the middle of the smallest and largest numbers.
# 4. The question my fourth function answers: "Is the average of the numbers in the list exactly in the middle between the smallest and largest numbers?" Splitting it into three functions makes it easier to check because each function can be tested independently, ensuring that they work correctly before combining them.


# Your code below
list = [4, 5, 6, 7, 8, 9]

# Fonction 1 : trouve le plus petit nombre
def plus_petit(liste):
    return min(liste)

# Fonction 2 : trouve le plus grand nombre
def plus_grand(liste):
    return max(liste)

# Fonction 3 : calcule la moyenne
def moyenne(liste):
    return sum(liste) / len(liste)

# Fonction 4 : utilise les trois autres
# Question : la moyenne est-elle pile au milieu entre le plus petit et le plus grand ?
def moyenne_au_milieu(liste):
    petit = plus_petit(liste)
    grand = plus_grand(liste)
    moy = moyenne(liste)
    milieu = (petit + grand) / 2
    return moy == milieu

# On affiche les résultats
print("Plus petit :", plus_petit(list))
print("Plus grand :", plus_grand(list))
print("Moyenne :", moyenne(list))
print("La moyenne est au milieu ?", moyenne_au_milieu(list))