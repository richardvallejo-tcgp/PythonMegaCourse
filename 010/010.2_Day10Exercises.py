'''
Day 10 Exercises
'''
folder = "010.0_Day10Files"

'''
Personal Test
'''
x = 0
while True:
    print("-----")
    print(x)
    try:
        y = int(input("Add: "))
        x = x + y
        if x < 10:
            print("Good job")
        elif x >= 10:
            print("I'm about to break!")
            break

    # We can access error text by passing it to the 'except' condition as below:
    except ValueError as e:
        print(e)

    # This 'else' condition runs only when there is no error
    else:
        print("Something else")

    # The 'finally' condition runs regardless of whether or not there is an error, and also runs before the 'break' above
    finally:
        print("Moving on")

print("-----")


'''
Code Experiments
'''
action = "test string"
try:
    # print(int(action[4:)) # This line missing the closing square bracket will not trigger an exception (not even 'except SyntaxError')
    print(int(action[4:]))

except ValueError: # This exception condition will catch a string when a number was expected, but will not catch a syntax error
    print("Value is not a number")

except SyntaxError: # This exception condition doesn't actually do anything for syntax error like a missing square bracket
    print("Oh no! We made a typo!")

print("-----")


'''
Bonus
'''
try:
    width = float(input("Enter rectangle width: "))
    height = float(input("Enter rectangle height: "))
    if width == height:
        exit("I didn't say square!")        

    area = width * height
    print(area)

except ValueError:
    print("Non-numeric input detected.")

print("-----")


'''
Coding Exercise 1
'''
try:
    value = float(input("Enter a single value data point: "))
    total = float(input("Enter the total sum of the dataset: "))
    if value > total:
        exit("Value cannot be greater than the total!")        

    percentage = (value / total) * 100
    print(percentage)

except ValueError:
    print("Non-numeric input detected.")

print("-----")


'''
Coding Exercise 2
'''
try:
    value = float(input("Enter a single value data point: "))
    total = float(input("Enter the total sum of the dataset: "))  

    percentage = (value / total) * 100
    print(percentage)

except ValueError:
    print("Non-numeric input detected.")

except ZeroDivisionError:
    print("Total cannot be 0.")

print("-----")


'''
Bug Fixing Exercise 1
'''
waiting_list = ["john", "marry"]
name = input("Enter name: ")

try: # Add a try block where we expect we might hit an error
    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")

except ValueError: # And add an exception block for the ValueError we saw
    print(f"{name} is not in the list")

print("-----")
