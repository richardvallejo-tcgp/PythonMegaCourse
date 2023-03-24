'''
Day 5 Exercises
'''
items = ['first', 'second', 'third']

# print(f"{index}: {item}") 'index' and 'item' variables have no declared value at this point
for index, item in enumerate(items):
    print(f"{index}: {item}")
print(f"{index}: {item}")
print(f"List length: {index+1}")
print(len(items))

new_string = "Hello"
for i, j in enumerate(new_string):
    print(i, j)

a = enumerate(items)
print(a)
a = list(a)
print(a)
for i, item in a:
    print(i, item)


'''
Bonus
'''
waiting_list = ["sen", "ben", "john"]

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)

waiting_list.sort() # List methods such as '.sort()' will modify the list without reassigning the variable

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)

print("Hello".replace("o", "x")) # The '.replace()' method returns the modified string

print(["c", "d", "b"].sort()) # The '.sort()' method returns a null value ("None")

mylist = ["c", "d", "b"]
mylist.sort()
print(mylist)

mylist.sort(reverse=True)
print(mylist)


'''
Coding Exercise 1
'''
filenames = ['document', 'report', 'presentation']
for x, fn in enumerate(filenames):
    print(f"{x}-{fn.capitalize()}.txt")


'''
Coding Exercise 2
'''
ips = ['100.122.133.105', '100.122.133.111']
ind_sel = int(input("Enter the index of the IP you want (0 or 1): "))
print(ips[ind_sel])


'''
Bug Fixing Exercise 1
'''
menu = ["pasta", "pizza", "salad"]
 
# user_choice = input("Enter the index of the item: ")
user_choice = int(input("Enter the index of the item: "))
 
message = f"You chose {menu[user_choice]}."
print(message)


'''
Bug Fixing Exercise 2
'''
menu = ["pasta", "pizza", "salad"]
 
# for i, j in enumerate[menu]:
for i, j in enumerate(menu):
    print(f"{i}.{j}")


'''
Bug Fixing Exercise 3
'''
menu = ["pasta", "pizza", "salad"]
 
for i, j in enumerate(menu):
    # print("f{i}.{j}")
    print(f"{i}.{j}")