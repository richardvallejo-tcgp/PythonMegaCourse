'''
Day 3 Exercises
'''

'''
Coding Experiment
'''

items = []

while True:
    user_action = input("Type 'Add', 'Show' or 'Exit': ")

    match user_action.lower().strip():
        case 'add' | 'new': # Matching on multiple cases
            user_input = input("Enter item: ")
            items.append(user_input)
        case 'show' | 'display':
            # Doing more in a For loop
            x = 0
            for item in items:
                item = item.title()
                print(x, item)
                x = x + 1
        case 'exit' | 'close':
            print("Closing")
            break
        case _: # Matching unexpected cases with a default
            print("Unexpected Input")


'''
Bonus
'''
meals = ['pasta', 'pizza', 'salad']

for meal in meals:
    print(meal.capitalize())

print("Bye")

for char in 'meals':
    print(char)


'''
Coding Exercise 1
'''
country = input("Enter the country you are from: ")

match country:
    case 'USA' | 'United States':
        print("Hello")
    case 'India':
        print("Namaste")
    case 'Germany':
        print("Hallo")
    case _:
        print("Hola")


'''
Coding Exercise 2
'''
ingredients = ["john smith", "sen plakay", "dora ngacely"]
for n in ingredients:
    print(n.title())


'''
Bug Fixing Exercise 1
'''
buttons = ["cancel", "reply", "submit"]
for i in buttons:
    print(i.capitalize())
 
# buttons = ["cancel", "reply", "submit"]


'''
Bug Fixing Exercise 2
'''
buttons = ["cancel", "reply", "submit"]
 
for i in buttons:
#print(i.capitalize())
    print(i.capitalize())


'''
Bug Fixing Exercise 3
'''
#for item in ["sandals", "glasses", "trousers"):
for item in ["sandals", "glasses", "trousers"]:
    #print(item.capitalize)
    print(item.capitalize())