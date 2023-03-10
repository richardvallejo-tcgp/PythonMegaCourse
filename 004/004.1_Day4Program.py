'''
Day 4 Program: Indexing, Integer and Float
'''
items = []

while True:
    user_action = input("Type 'Add', 'Edit', 'Show' or 'Exit': ")

    match user_action.lower().strip():
        case 'add':
            user_input = input("Enter an item: ")
            items.append(user_input)
        case 'edit':
            x = 0 # Use variable 'x' as an index counter
            for item in items:
                print(x, item)
                x = x + 1
            item_index = int(input("Enter an index to edit: ")) # int() creates an integer, float() creates a decimal number
            user_input = input("Enter the new item: ")
            items[item_index] = user_input
        case 'show':
            for item in items:
                print(item)
        case 'exit':
            print('Closing')
            break
