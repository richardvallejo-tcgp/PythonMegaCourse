'''
Day 6 Program: Writing and Reading Text Files
'''
filename = "006.0_Day6Data.txt"

while True:
    user_action = input("Type 'Add', 'Edit', 'Show', 'Complete' or 'Exit': ")

    match user_action.lower().strip():
        case 'add':
            user_input = input("Enter an item: ")

            file = open(filename, 'r')
            items = file.readlines()
            file.close()

            items.append(f"{user_input}\n")

            file = open(filename, 'w')
            file.writelines(items)
            file.close()
        case 'edit':
            file = open(filename, 'r')
            items = file.readlines()
            file.close()
            for index, item in enumerate(items): # Using the 'enumerate()' function on a list provides an index for each list item in addition to its value
                # f-Strings allow for setting the value of a string using a combination of normal text and variable or expression values
                # Variable or Expression values need to be enclosed in curly brackets '{}'
                item = item
                print(f"{index}-{item}")

            item_index = int(input("Enter an index to edit: ")) # int() creates an integer, float() creates a decimal number
            user_input = input("Enter the new item: ")
            items[item_index] = f"{user_input}\n"

            file = open(filename, 'w')
            file.writelines(items)
            file.close()
        case 'show':
            file = open(filename, 'r')
            items = file.readlines()
            file.close()
            for index, item in enumerate(items):
                item = item
                print(f"{index}-{item}")
        case 'complete':
            file = open(filename, 'r')
            items = file.readlines()
            file.close()
            for index, item in enumerate(items):
                item = item
                print(f"{index}-{item}")
            item_select = int(input("Enter an index to complete: "))
            items.pop(item_select) # '.pop()' defaults to removing the last item in the list, or can be passed an index to remove
            # The '.remove()' method expects the value of a list item to remove rather than an index
            # item_select = input("Enter an item to complete: ")
            # items.remove(item_select) # This will remove the first list item with a matching value
            
            file = open(filename, 'w')
            file.writelines(items)
            file.close()
        case 'exit':
            print('Closing')
            break
