'''
Day 3 Program: Match Case, For Loops
'''
items = []

while True:
    user_action = input("Type 'Add', 'Show' or 'Exit': ")

    match user_action.lower().strip():
        case 'add':
            user_input = input("Enter an item: ")
            items.append(user_input)
        case 'show':
            for item in items:
                print(item)
        case 'exit':
            print('Closing')
            break
