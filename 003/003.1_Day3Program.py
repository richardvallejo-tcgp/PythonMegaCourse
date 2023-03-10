'''
Day 3 Program: Match Case, For Loops
'''
items = []

while True:
    user_action = input("Type 'Add', 'Show' or 'Exit': ")

    match user_action.lower().strip(): # Using 'lower()' and 'strip()' allows for more flexible matching regardless of upper/lower case or whitespace
        case 'add':
            user_input = input("Enter an item: ")
            items.append(user_input)
        case 'show':
            for item in items:
                print(item)
        case 'exit':
            print('Closing')
            break # 'break' forces out of the For loop
