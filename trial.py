import math
import random
'''
def print_name():
    """When called will print name""" #if you type help(print_name) it will print that
    name = "Emma E. Moritz"
    return name


def volume_sphere(radius):
    volume=4/3*math.pi*radius**3
    return volume

def myprogram():
    v=volume_sphere(2)
    print(v)
____________________________________________________________________________
'''
def volume_cyl(radius,height,cans):
    """This is a function to clculate the volume of a cylinder"""
    volume=height*math.pi*radius**2*cans
    print(volume)
def main():
    volume_cyl(1.31,4.75,20)

if __name__ == "__main__":
    main()
