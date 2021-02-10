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


def min(a, b, c):
    if type(a) == str:
        frst = ord(a)
    else:
        frst = a
    if type(b) == str:
        scnd = ord(b)
    else:
        scnd = b
    if type(c) == str:
        thrd = ord(c)
    else:
        thrd = c
    if (frst-scnd) <= 0 and (frst-thrd) <= 0:
        num = a
        return num
    elif (scnd-frst) <= 0 and (scnd-thrd) <= 0:
        num = b
        return num
    else:
        num = c
        return num

def main():
    print(min(7, 3, 5))
    print(min(5, 5, 4))
    print(min(2, 2, 3))
    print(min(-2, -6, -100))
    print(min("Z", "B", "A"))

if __name__ == "__main__":
    main()