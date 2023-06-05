'''
Day 13 Exercises
'''
folder = "013.0_Day13Files"
bonus = "013.0.2_Day13BonusData.txt"

'''
Code Experiments
'''
# Previously, we would have needed to do something like this for a multi-line string:
text_1 = "\
This is a multi-line string.\
This string spans multiple lines.\
This string contains more than one line.\
In fact, this string has several lines.\
"
print(text_1)

# Using triple quotes, we can simplify this by eliminating the need for ending every line with a backslash.
text_2 = """
This is a multi-line string.
This string spans multiple lines.
This string contains more than one line.
In fact, this string has several lines.
"""
print(text_2)


'''
Bonus
'''
feet_inches = input("Enter feet and inches: ")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet_part = float(parts[0])
    inches_part = float(parts[1])
    inches_total = inches_part + (feet_part * 12)
    feet_total = inches_total / 12
    return {"feet": feet_part, "inches": inches_part, "feet_total": feet_total, "inches_total": inches_total}


def convert(us_std):
    meters = us_std["inches_total"] * 0.0254
    return meters


parsed = parse(feet_inches)
result = convert(parsed)

if result < 1:
    print("Yer too small, kid!")
else:
    print("Get on the ride already!")


'''
Coding Exercise 1
'''
def age_calc(year_of_birth, current_year = 2023):
    return current_year - year_of_birth


print(age_calc(1987))


'''
Coding Exercise 2
'''
user_input = input("What is the year of your birth? ")
age = age_calc(int(user_input))
# print(age)


'''
Coding Exercise 3
'''
if age > 120:
    print("Looking good for your age.")


'''
Coding Exercise 3
'''
def get_names(name_input = input("Enter names separated by commas (no spaces): ")):
    names = name_input.split(",")
    return names


names = get_names()
print(len(names))


'''
Bug Fixing Exercise 1
'''
# def calculate_time(g=9.80665, h): # Default value parameters must come after non-default parameters
def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t

  
time = calculate_time(100)
print(time)
