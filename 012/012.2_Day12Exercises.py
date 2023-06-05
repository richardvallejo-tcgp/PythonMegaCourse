'''
Day 12 Exercises
'''
folder = "012.0_Day12Files"
bonus = "012.0.2_Day12BonusData.txt"

'''
Code Experiments
'''
def test_function_1(in_var, app):
    in_var = str(in_var) + str(app)
    return in_var


varg = "Original String"
varg = test_function_1(varg, "*")
print(varg)
# varg = test_function_1(in_var=varg, "*") # This line produces an error because a positional argument cannot follow a keyword argument
varg = test_function_1(varg, app="*")
print(varg)
# varg = test_function_1(in_var_new=varg) # This line produces an error because there is no 'in_var_new' parameter
varg = test_function_1(app="*", in_var=varg) # When using keyword arguments, order does not matter
print(varg)
varg = test_function_1("*", varg) # When using positional arguments, order does matter
print(varg)


'''
Bonus
'''
feet_inches = input("Enter feet and inches: ")

def convert(us_std):
    parts = us_std.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    inches = inches + (feet * 12)
    feet = inches / 12
    meters = inches * 0.0254
    print(inches, "inches")
    print(feet, "feet")
    print(feet * 0.3048, "feet to meters")
    print(meters, "inches to meters")
    return meters


result = convert(feet_inches)

if result < 1:
    print("Yer too small, kid!")
else:
    print("Get on the ride already!")


'''
Coding Exercise 1
'''
def l_to_m3(l):
    l = float(l)
    return l / 1000


liters = input("Enter a volume in liters: ")
print(l_to_m3(liters), "cubic meters")


'''
Coding Exercise 2
'''
def pw_check(test):
    if len(test) >= 8 and True in [c.isupper() for c in test] and True in [c.isdigit() for c in test]:
        print("Strong Password")
    else:
        print("Weak Password")


user_pass = input("Enter new password: ")
pw_check(user_pass)


'''
Bug Fixing Exercise 1
'''
def speed(distance, time):
    return distance / time
    
# print(speed([200, 4]))
print(speed(200, 4))


'''
Bug Fixing Exercise 2
'''
def speed(distance, time):
    return distance / time
    
# print(speed(5, 300))
print(speed(time=5, distance=300)) # Using keyword arguments
print(speed(300, 5)) # Alternative with positional arguments
