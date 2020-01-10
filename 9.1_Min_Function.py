'''
MIN FUNCTION
------------
Write a function called min that will take three numbers as parameters 
and return the smallest value. If more than one number is tied for smallest, 
still return that smallest number. Once you've finished writing your function, 
copy/paste the following code and make sure that it runs correctly with the function you created:

INPUT
-----
print(min(7, 3, 5))
print(min(5, 5, 4))
print(min(2, 2, 3))
print(min(-2, -6, -100))
print(min("Z", "B", "A"))

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
def min(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        small = num1
        return num1
    if num2 < num1 and num2 < num3:
        small = num2
        return num2
    if num3 < num1 and num3 < num2:
        small = num3
        return num3
    if num1 and num2 < num3:
        small = num1
        return num1

print(min(7, 3, 5))
print(min(5, 5, 4))
print(min(2, 2, 3))
print(min(-2, -6, -100))
print(min("Z", "B", "A"))