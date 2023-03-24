'''
Day 9 Exercises
'''
folder = "009.0_Day9Files"

'''
Code Experiments
'''
coin_flip = input("Flip a coin and enter 'heads' or 'tails': ")

if coin_flip == 'heads' or coin_flip == 'tails':
    print(coin_flip)
else:
    print("Invalid entry")

if coin_flip != 'heads' and coin_flip != 'tails':
    print("Invalid entry")
else:
    print(coin_flip)

valid_options = ['heads', 'tails']
if coin_flip not in valid_options:
    print("Invalid entry")
else:
    print(coin_flip)


'''
Bonus
'''
password = input("Enter new password: ")

# Perform checks using a list
pw_check = [len(password) > 8, True in [c.isdigit() for c in password], True in [c.isupper() for c in password]]

if all(pw_check):
    print("Muy Fuerte")

else:
    print("WEAK")
    if not pw_check[0]:
        print("Password should be greater than 8 characters in length.")

    if not pw_check[1]:
        print("Password should contain at least one digit.")

    if not pw_check[2]:
        print("Password should contain at least one uppercase character.")

# Perform checks using a dictionary
pw_check = {'length': len(password) > 8, "numeric": True in [c.isdigit() for c in password], "uppercase": True in [c.isupper() for c in password]}

if all(pw_check.values()):
    print("Muy Fuerte")

else:
    print("WEAK")
    if not pw_check["length"]:
        print("Password should be greater than 8 characters in length.")

    if not pw_check["numeric"]:
        print("Password should contain at least one digit.")

    if not pw_check["uppercase"]:
        print("Password should contain at least one uppercase character.")


'''
Coding Exercise 1
'''
password = input("Enter a new password: ")
if len(password) > 7:
    print("Great password there!")
else:
    print("Your password is weak.")


'''
Coding Exercise 2
'''
password = input("Enter a new password: ")
length = len(password)
if length > 7:
    print("Great password there!")
elif length == 7:
    print("Password is OK, but not too strong")
else:
    print("Your password is weak.")


'''
Bug Fixing Exercise 1
'''
ids = ["XF345_89", "XER76849", "XA454_55"]
 
x = 0
 
# for id in ids:
# if '_' in id:
    # x = x + 1
for id in ids:
    if '_' in id:
        x = x + 1
print(x)


'''
Bug Fixing Exercise 2
'''
ids = ["XF345_89", "XER76849", "XA454_55"]
 
x = 0
 
for id in ids:
    if '_' in id:
        x = x + 1
    # print(x)

print(x)


'''
Bug Fixing Exercise 3
'''
length = float(input("Enter length: "))
width = float(input("Enter width: "))
 
perimeter = (length + width) * 2
area = length * width
 
print("Perimeter is", perimeter)
print("Area is", area)
 
# if perimeter < 14 and area > 10:
if perimeter < 14 and area < 8:
    print("OK")
else:
    print("NOT OK")
