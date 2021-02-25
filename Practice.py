def count_list(my_list,key):
    x=0
    for i in range(len(my_list)):
        if my_list[i]==key:
            x+=1
    print("Found",key,x,"times")

my_list = [1, 2, 3, 3, 3, 4, 2, 1]
count_list(my_list, 3)
