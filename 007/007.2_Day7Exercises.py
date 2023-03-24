'''
Day 7 Exercises
'''
'''
Bonus
'''
filenames = ["1.doc", "1.report", "1.presentation"]
filenames = [f"{filename.replace('.', '-')}.txt" for filename in filenames]
print(filenames)


'''
Coding Exercise 1
'''
names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]
print(names)


'''
Coding Exercise 2
'''
usernames = ["john 1990", "alberta1970", "magnola2000"]
lengths = [len(username) for username in usernames]
print(lengths)


'''
Coding Exercise 3
'''
user_entries = ['10', '19.1', '20']
floats = [float(i) for i in user_entries]
print(floats)


'''
Coding Exercise 4
'''
user_entries = ['10', '19.1', '20']
floats = [float(i) for i in user_entries]
print(sum(floats))


'''
Bug Fixing Exercise 1
'''
temperatures = [10, 12, 14]
temperatures = [f"{str(temp)}\n" for temp in temperatures] # Convert to strings and add linebreaks
file = open("file.txt", 'w')
 
file.writelines(temperatures)
file.close() # Close the file


'''
Bug Fixing Exercise 2
'''
numbers = [10.1, 12.3, 14.7]
# numbers = [int(number) for item in numbers]
numbers = [int(number) for number in numbers]
print(numbers)
