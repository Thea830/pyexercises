"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: here, the function receives a list of numbers
# 2. Process: the function calculates the average of the numbers in the list by summing them up and dividing by the length of the list
# 3. Out:  the function returns the average of the numbers in the list
# # 4. My function name, and why return rather than print: explains what the function does, and it returns the result rather than printing it so that the result can be used later in the program or stored in a variable for further processing.


# Your code below
list = [4, 5, 6, 7, 8, 9]

# Fonction qui calcule la moyenne d'une liste
def moyenne(liste):
    total = sum(liste)
    return total / len(liste)

# On appelle la fonction trois fois avec des listes différentes
resultat1 = moyenne(list)
resultat2 = moyenne([1, 2, 3])
resultat3 = moyenne([10, 20, 30, 40])

# On affiche les trois résultats
print("Moyenne 1 :", resultat1)
print("Moyenne 2 :", resultat2)
print("Moyenne 3 :", resultat3)



