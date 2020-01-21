import math

'''def print_name():
    """When called will print name""" #if you type help(print_name) it will print that
    name = "Emma E. Moritz"
    return name'''




def volume_sphere(radius):
    volume=4/3*math.pi*radius**3
    print(f"Your volume is: {volume:.2f} m^3")

def myprogram():
    volume_sphere(2)

if __name__ == "__main__":
    myprogram()
