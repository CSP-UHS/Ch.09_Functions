import random

def create_list(x):
    list=[]
    for i in range(x):
        num = random.randint(1,6)
        list.append(num)
    return list


def count_list(list,x):
    count = 0
    for item in list:
        if item == x:
            count += 1
    return count


def average_list(list):
    sum = 0
    for item in list:
        sum += item
    avg = sum/len(list)
    return avg




def myprogram():
    my_list = create_list(10000)
    for i in range(1,7):
        print("There are",count_list(my_list,i),"amount of",i,"'s.")
    print(float(average_list(my_list)))


if __name__ == '__main__':
    myprogram()





