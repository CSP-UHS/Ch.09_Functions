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

nlist = ()
def mini(n1,n2,n3):
  if n1 <= n2 and n1 <=n3:
      return n1
  elif n2 <= n1 and n2 <= n3:
      return n2
  elif n3 <= n2 and n3 <= n1:
      return n3

def main():
    print(mini(7, 3, 5))
    print(mini(5, 5, 4))
    print(mini(2, 2, 3))
    print(mini(-2, -6, -100))
    print(mini("Z", "B", "A"))

if __name__=="__main__":
    main()