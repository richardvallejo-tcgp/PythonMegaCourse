'''
Day 2 Program: While Loops and Methods
'''
user_prompt = "Enter an item: "

items = [] # Create an empty List to add to later on.
user_input = "" # Create an empty String so that we can use the length as an exit condition for the loop

# Create a loop for multiple item entry.
while len(user_input) == 0:
    # Indent all code to run in the loop. White space matters in Python!
    user_input = input(user_prompt)
    print("Capitalize:", user_input.capitalize()) # '.capitalize()' is a Method of the String data type.
    print("Title:", user_input.title()) # '.title()' is another Method of the String data type.
    print("Raw:", user_input)
    user_input = user_input.title()
    items.append(user_input) # '.append()' is a Method of the List data type. The 'user_input' variable is passed to it as an Argument.
    print("Modified", user_input)
    print("List", items)
    print("Next...")