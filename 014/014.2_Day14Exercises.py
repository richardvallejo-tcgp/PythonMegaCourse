'''
Day 14 Exercises
'''
folder = "014.0_Day14Files"
bonus = "014.0.2_Day14BonusData.txt"

'''
Code Experiments
'''
import exercises


'''
Bonus
'''
feet_inches = input("Enter feet and inches: ")

parsed = exercises.parse(feet_inches)
metric = exercises.convert(parsed)
print(exercises.check_height(metric, 1))


'''
Coding Exercise 1
'''
input_temp = float(input("Enter water temperature: "))
print(exercises.check_state(input_temp))


'''
Bug Fixing Exercise 1
'''
import exercises
 
# nr_of_periods = count("Trees are good. Grass is green.")
nr_of_periods = exercises.count("Trees are good. Grass is green.")
print(nr_of_periods)


'''
Bug Fixing Exercise 2
'''
# import exercises.py
import exercises
 
nr_of_periods = exercises.count("Trees are good. Grass is green.")
print(nr_of_periods)


'''
Bug Fixing Exercise 3
'''
from exercises import count
 
# nr_of_periods = functions.count("Trees are good. Grass is green.")
nr_of_periods = count("Trees are good. Grass is green.")
print(nr_of_periods)