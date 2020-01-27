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
def min(A,B,C):
    '''This function will pint the smallest of the 3 given numbers'''
    if A<B and A<C:
        return A
    elif B<A and B<C:
        return B
    elif C<A and C<B:
        return C
    elif A==B and A<C:
        return A
    elif B==C and B<A:
        return B
    elif C == A and C < B:
        return C

def nummin():
    print(min(-100,-2,-5))

if __name__ == "__main__":
    nummin()