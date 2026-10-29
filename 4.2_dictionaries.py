"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a person's name, age, city, country
# 2. Process: reading the values, changing the age, removing a field, and displaying every field with it's value
# 3. Out: displaying the person's name, age, city, country, updated age, and remaining fields 
# 4. My object, my five fields, and why those: a person, the five fields are name, age, city, country, and updated age. i chose those fields because they are basic information about a person and are commonly used in many aapplications, 


# Your code below
name = input("enter your name: ")
age = input("emter your age: ")
city = input("enter your city: ")
country = input("enter your country: ")

print("My name is", name)
print("My age is", age)
print("My city is ", city)
print("My country is", country)

person = {
    "name": name,
    "age": age, 
    "city": city, 
    "country": country,
}

print("the person's name is: ", person["name"])
print("the person's age is: ", person["age"])
print("the person's city is: ", person["city"])
print("the person's country is: ", person["country"])

person["age"]= input("enter your new age: ")
print("updated age: ", person["age"])
print("the person's remaining fields are: ", person)
