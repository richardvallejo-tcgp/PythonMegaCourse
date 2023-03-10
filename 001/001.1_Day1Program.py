'''
Day 1 Program: Variables, Data Types and Inputs
'''
user_prompt = "Enter an item to do: " # Storing a String in a Variable

user_text1 = input(user_prompt) # 'input()' is a Function. Its return value will be stored in the Variable
user_text2 = input(user_prompt)
user_text3 = input(user_prompt)

items = [user_text1, user_text2, user_text3, "Another String"] # Store multiple values in a List

print(items)

print(type(items))