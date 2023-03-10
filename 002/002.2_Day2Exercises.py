'''
Day 2 Exercises
'''

'''
Bonus
'''
password = input("Enter password: ")

while password != "pass123":
    password = input("Enter password: ")

print("Password was correct!")

x = 1

while x <= 6:
    print(x)
    x = x + 1


'''
Coding Exercise 1
'''
name_input = input("Type Your Name: ")
print("Exercise 1:", name_input.capitalize())


'''
Coding Exercise 2
'''
name_input = input("Type Your Name: ")
name_input = name_input.capitalize()
n = 0

while n < 5:
    print("Exercise 2:", n, name_input)
    n = n + 1


'''
Coding Exercise 3
'''
n = 0

while n < 5:
    name_input = input("Type Your Name: ")
    print("Exercise 3:", name_input.capitalize())
    n = n + 1


'''
Bug Fixing Exercise 1
'''
# while True
# print("Hello")

test = True

while test:
    print("Bug Fix 1:", "Hello")
    test = False


'''
Bug Fixing Exercise 2
'''
greeting = "hello"
# print(upper(greeting))
print("Bug Fix 2:", greeting.upper())


'''
Bug Fixing Exercise 3
'''
countries = []
test = True

while test:
    country = input("Enter the country: ")
    countries.append(country)
    print("Bug Fix 3:", countries)
    test = False
# print(countries)


'''
Programming Tool: Listing available methods
'''
print("String:", dir(str))
print("asdf:", dir("asdf"))
help(str.capitalize)
print("List:", dir(list))
help(list.append)

import builtins
print("Builtins:", dir(builtins))