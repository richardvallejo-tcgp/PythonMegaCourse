'''
Day 11 Exercises
'''
folder = "011.0_Day11Files"
bonus = "011.0.2_Day11BonusData.txt"

'''
Code Experiments
'''
def greet():
    message = "ho ho"
    new_message = message.capitalize()
    print("hey hey")
    return new_message


greeting = greet()
print(greeting)
print(greet())


'''
Bonus
'''
def get_average():
    with open(f"{folder}/{bonus}") as file:
        data = file.readlines()
    
    values = [float(d.strip("\n")) for d in data[1:]]

    average_loc = sum(values) / len(values)
    return average_loc


average = get_average()
print(average)


'''
Coding Exercise 1
'''
def get_max():
    grades = [9.6, 9.2, 9.7]
    return max(grades)


print(get_max())


'''
Coding Exercise 2
'''
def get_min():
    grades = [9.6, 9.2, 9.7]
    return min(grades)


def get_max():
    grades = [9.6, 9.2, 9.7]
    return max(grades)


print(f"Max: {get_max()}, Min: {get_min()}")


'''
Bug Fixing Exercise 1
'''
def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    # print(maximum)
    # No return value
    return maximum


celsius = get_maximum()
 
fahrenheit = celsius * 1.8 + 32
print(fahrenheit)
