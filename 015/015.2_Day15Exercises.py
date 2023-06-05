'''
Day 15 Exercises
'''
import exercises
folder = "015.0_Day15Files"
bonus = "015.0.2_Day15BonusData.txt"

'''
Code Experiments
'''
import glob
import csv
import shutil
import webbrowser

# Read all txt files
myfiles = glob.glob(f"{folder}/*.txt")
print(myfiles)

for filepath in myfiles:
    with open(filepath, "r") as file:
        print(filepath)
        print(file.read())
        print("\n\n")

# Parse csv files
mycsvs = glob.glob(f"{folder}/*.csv")
print(mycsvs)

for filepath in mycsvs:
    with open(filepath, "r") as file:
        data = list(csv.reader(file))
    
    print(data)
    print(data[2][1])
    print("\n\n")

cities = [row[0] for row in data][1:]
city = input(f"Enter a city [{', '.join(cities)}]: ")
print(data[cities.index(city)+1][1])

# Zip files
shutil.make_archive("output", "zip", folder)

# Web browser search
user_term = input("Enter a search term: ")
webbrowser.open(f"https://google.com/search?q={user_term.replace(' ', '+')}")


'''
Bonus
'''
import json
with open(f"{folder}/questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

print(type(content))
print(type(data))
results = []

for q in data:
    print(q["question"])
    for i, o in enumerate(q["options"]):
        print(f"{i+1}: {o}")
    q["choice"] = int(input("Enter the number of your selected answer: "))

score = [q["answer"]==q["choice"] for q in data].count(True) / len(data)
print(f"You scored {int(score * 100)}%")

for i, q in enumerate(data):
    result = "Incorrect"
    if q["choice"]==q["answer"]:
        result = "Correct"
    message = f"""Question #{i+1} - {result}
    You answered: {q["choice"]} ({q["options"][q["choice"]-1]})
    Correct answer: {q["answer"]} ({q["options"][q["answer"]-1]})
    """
    print(message)


'''
Coding Exercise 1
'''
bounds = exercises.bounds_prompt()
print(exercises.get_random_int(bounds))


'''
Bug Fixing Exercise 1
'''
from parsers import parse 
import random
 
# Ask the user to enter a lower and an upper bound divided by a comma
user_input = input("Enter a lower bound and an uppwer bound divided a comma (e.g., 2,10)")
 
# Parse the user string by calling the parse function
parsed = parse(user_input)
 
# Pick a random int between the two numbers
rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])
 
print(rand)
