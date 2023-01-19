mylist = [2,10,5,98]

mytuple = (255,234,212)

print(type(mytuple))

droids = [34, "C3PO", True, [1,5,6]]
print(droids)
droids[1] = "K2SO"

print(len(droids))
print(droids[3][1]) #3rd index of the first list. 2nd index of the list inside that list.

for i in range(len(droids)):
    print(type(droids[i]))

nat_league_top3 = [["Mets","Nationals","Braves"],["Cardinals","Pirates","Cubs","Rads"],["Dodgers","Giants","Diamondbacks"]]

nat_league_top3[1].append("Losers") #add an item to the end of particular list
nat_league_top3[1].pop() #remove the last item from a particular list
team = nat_league_top3[1].pop() #assign the last item from list to a variable
print(nat_league_top3)
print(team)
'''
Create a custom list:
my_list=[]
for i in range(5):
    num=int(input("Enter an integer:"))
    my_list.append(num)
print(my_list)

#Add an amount to each item in the list:
for i in range(len(my_list)):
    my_list[i]+=2
print(my_list)
'''
#String and modifying the string
uhs_slogan = "My school is the best"
print(uhs_slogan[:13] + "awesome")

#cut parts off the code
email = "abc@urbandaleschools.com"
username=''
for letter in email:
    if letter == "@":
        break
    else:
        username+=letter
print(username)
