import math


def volume_sphere(radius):
    ''' calculates the volume of a sphere '''
    volume = 4/3 * math.pi * radius ** 3
    return volume


def volume_cylinder(r, h):
    volume = math.pi * r ** 2 * h
    return volume


def hyp(leg1, leg2):
    hypot = math.sqrt(leg1 ** 2 + leg2 ** 2)
    print(hypot)


def mean(list):
    total = 0
    for item in list:
        total += item
    avg = total/len(list)
    print(avg)


def perimeter(b, h):
    per = 2 * b + 2 * h
    print(per)


def myprogram():
    hyp(1, 2)
    perimeter(4, 5)


if __name__ == "__main__":
    myprogram()
