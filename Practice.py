import random
def create_list(x):
    while x>0:
        x-=1
        num=random.randrange(0,7)
        my_list.append(num)

my_list=[]
create_list(10000)
print(my_list)

def count_list(my_list,key):
    x=0
    y=0
    n=0
    p=0
    g=0
    t=0
    for i in range(len(my_list)):
        if my_list[i]==1:
            x+=1
        elif my_list[i]==2:
            y+=1
        elif my_list[i]==3:
            n+=1
        elif my_list[i]==4:
            p+=1
        elif my_list[i]==5:
            g+=1
        else:
            t+=1
    print("Found",1,x,"times")
    print("Found", 2, y, "times")
    print("Found", 3, n, "times")
    print("Found", 4, p, "times")
    print("Found", 5, g, "times")
    print("Found", 6, t, "times")

count_list(my_list, 1)

def average_list(my_list):
    sum=0
    for i in my_list:
        sum+=i
        average=sum/len(my_list)
    print(average)

average_list(my_list)