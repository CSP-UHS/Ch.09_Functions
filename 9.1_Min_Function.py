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


def mini(x, y, z):
    if x < y and x < z:
        minimum = x
    elif y < x and y < z:
        minimum = y
    else:
        minimum = z
    return minimum


def main():
    num1 = input('Enter number: ')
    num2 = input('Enter number: ')
    num3 = input('Enter number: ')

    print(mini(num1, num2, num3))


if __name__ == "__main__":
    main()
