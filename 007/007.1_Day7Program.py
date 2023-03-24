'''
Day 7 Program: List Comprehension
'''
filename = "007.0_Day7Files/007.0.1_Day7Data.txt"

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
            
            # The first solution to cleaning our list of strings is to create a new list to populate
            items_cleaned = []
            # Populate the list with one for loop on our 'items' list
            for item in items:
                items_cleaned.append(item.strip('\n'))
            # Now that we have a list of cleaned strings, use a for loop on the new list to display the items
            for index, item in enumerate(items_cleaned):
                print(f"{index}-{item}")

            item_index = int(input("Enter an index to edit: "))
            user_input = input("Enter the new item: ")
            items[item_index] = f"{user_input}\n"

            file = open(filename, 'w')
            file.writelines(items)
            file.close()
        case 'show':
            file = open(filename, 'r')
            items = file.readlines()
            file.close()

            # The second solution to cleaning our list of strings is with list comprehension syntax
            items_cleaned = [item.strip('\n') for item in items]
            # Now we have a list of cleaned strings to loop over
            for index, item in enumerate(items_cleaned):
                print(f"{index}-{item}")
        case 'complete':
            file = open(filename, 'r')
            items = file.readlines()
            file.close()

            # The third solution is to reassign the 'item' variable within the for loop on the initial list as read from the file
            for index, item in enumerate(items):
                item = item.strip('\n')
                print(f"{index}-{item}")
            item_select = int(input("Enter an index to complete: "))
            items.pop(item_select)
            
            file = open(filename, 'w')
            file.writelines(items)
            file.close()
        case 'exit':
            print('Closing')
            break
