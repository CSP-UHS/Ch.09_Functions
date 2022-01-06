'''
MINI FUNCTION
------------
Write a function called mini that will take three numbers as parameters 
and return the smallest value. If more than one number is tied for smallest, 
still return that smallest number. Once you've finished writing your function, 
copy/paste the following code and make sure that it runs correctly with the function you created:

INPUT
-----
print(mini(7, 3, 5))
print(mini(5, 5, 4))
print(mini(2, 2, 3))
print(mini(-2, -6, -100))
print(mini("Z", "B", "A"))

OUTPUT
------
3
4
2
-100
A

The function should return the value, not print the value. 
Also, while there is a min function built into Python, don't use it. 
Please use if statements and practice creating it yourself.
'''
import random
def mini():
    first_number=float(input("Enter a number"))
    second_number=float(input("Enter another number"))
    third_number=float(input("Enter a final number"))
    if first_number<second_number and first_number<third_number:
        print(first_number)
    if second_number<first_number and second_number<third_number:
        print(second_number)
    if third_number<first_number and third_number<second_number:
        print(third_number)
mini()