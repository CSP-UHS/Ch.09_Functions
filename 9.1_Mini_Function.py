'''
MINI FUNCTION
------------
Write a function called mini that will take three numbers as parameters 
and return the smallest value. If more than one number is tied for smallest, 
still return that smallest number. Once you've finished writing your function, 
copy/paste the following code and make sure that it runs correctly with the function you created:

INPUT
-----
'''
def mini(x,y,z):
    # if x<y and x<z or x<y and x==z or x<z and x==y:
    #     print(x)
    # elif y<x and y<z or y<x and y==z or y<z and y==x:
    #     print(y)
    # elif z<x and z<y or z<x and z==y or z<y and z==x:
    #     print(z)
    if x <= y and x <= z:
        return x
    elif y <= x and y <= z:
        return y
    else:
        return z

print(mini(7, 3, 5))
print(mini(5, 5, 4))
print(mini(2, 2, 3))
print(mini(-2, -6, -100))
print(mini("Z", "B", "A"))



'''

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
