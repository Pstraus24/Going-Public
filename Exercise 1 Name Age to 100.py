# Exercise 1 (and Solution)
"""Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and
printing out that many copies of the previous message.
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)"""
import datetime


def CalculateAge():

    now = datetime.datetime.now()
    today = now.year
    return today

def how_often():
    print_runs = int(input('\nok. Now enter a number between 1 and 10: '))
    if print_runs < 1 or print_runs > 10:
        print("C'mon, between 1 and 10 please ")
        how_often()
    return print_runs


i = 1
user_name = input("Enter your full name: ")
user_age = int(input('Enter your present age: '))
this_year = int(CalculateAge())
count_to = this_year + (100 - user_age)
print_this = "Hello " + user_name + "\nThought you might like to know that you will not be 100 years old until " + str(count_to)
print(print_this)
print_count = how_often()
while i <= print_count:
    print(i, print_this)
    i += 1

print("The End")
    

