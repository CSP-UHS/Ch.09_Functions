import math


def volume_sphere(radius):
    """This function calculates the volume of a sphere"""
    volume = 4 / 3 * math.pi * math.pow(radius, 3)
    print(f"the volume the sphere is...{volume:.2f} in^3")


def volume_cyl(r, h):
    volume = math.pi * math.pow(r, 2) * h
    return volume


def hyp(leg1, leg2):
    hypot = math.sqrt(leg1 ** 2 + leg2 ** 2)
    print(hypot)


def mean(list):
    total = 0
    for item in list:
        total += item
    ave = total / len(list)

    print(ave)


def perimeter(b, h):
    per = 2 * b + 2 * h
    print(per)


def myprogram():
    hyp(4, 7)
    numlist = [13, 2, 54, 23, 34, 71]
    mean(numlist)
    perimeter(4, 5)


print(__name__)
if __name__ == "__main__":
    myprogram()
