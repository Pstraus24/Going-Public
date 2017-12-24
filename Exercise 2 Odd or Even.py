"""
Exercise 2 (and Solution)
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:

Function extra_one(): If the number is a multiple of 4, print out a different message.
Function extra_two(): Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

#  ----------------- Define function extra_one to determine if user number is divisible by 4 -------
def extra_one(self):
    if (self % 4) == 0:
        #  ------------- Sassy comment to inform that number is divisible by 4 --------------
        print("Is this a leap year?\n")

#  ---------- Define/execute function to get two values from user and check for odd/even quotient --
def extra_two():
    print("Let's make this a little more interesting.")
    num = int(input("Enter a number between 1 and 10,001 (Note: Do NOT use a comma): "))
    check = int(input("And now enter another number between 1 and 10,000: "))
    if (num % check) != 0:
        print(check, "does NOT divide evenly into", num)
        print("There is a remainder of ", (num % check))
    else:
        print("What do ya know? ", check, "DOES divide evenly into ", num)



def main():
    user_input = int(input("Enter a number between 1 and 10,000: "))

    if (user_input % 2) != 0:
        print("You have entered an odd number")
    else:
        print("You have entered an even number")
        extra_one(user_input)
    extra_two()


main()
print("The End")
