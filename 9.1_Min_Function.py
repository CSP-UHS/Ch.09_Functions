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

def min(a,b,c):
    if a==b and a<c:
        return a
    elif a==c and a<b:
        return a
    elif b==c and b<a:
        return b
    elif a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    elif c<a and c<a:
        return c

def main():
    print(min(7, 3, 5))
    print(min(5, 5, 4))
    print(min(2, 2, 3))
    print(min(-2, -6, -100))
    print(min("Z", "B", "A"))

if __name__ == "__main__":
    main()