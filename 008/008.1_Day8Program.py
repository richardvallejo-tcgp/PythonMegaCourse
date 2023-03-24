'''
Day 8 Program: 'With' Context Manager
'''
print("Starting...")

# Define the filename pattern
course_day = "8"
filename = f"{(3 - len(course_day)) * '0'}{course_day}.0_Day{course_day}Files/{(3 - len(course_day)) * '0'}{course_day}.0.1_Day{course_day}Data.txt"

# Avoid repeating the open/read code block multiple times
with open(filename, 'r') as file:
    items = file.readlines() # Create our items list which can be modified and written back to the file periodically

# I want to start each execution by displaying the saved list of items
user_action = "Show"

while True:
    # Define our message to display at the end of the loop
    message = "End of request"
    user_action = user_action.lower().strip() # Enable flexible matching by forcing any input to lowercase and remove whitespace

    match user_action:
        case 'show': # Because the script sets "Show" as the option initially, this will always run first
            print("---")

            # I like this method for removing line breaks because we are performing other operations during the for loop
            for index, item in enumerate(items):
                item = item.strip('\n')
                print(f"{index}-{item}")

            message = "---"

        case 'add':
            user_input = input("Enter an item: ")
            items.append(f"{user_input}\n")
            message = f"Item {len(items)-1} '{user_input}' was added to the list."

        case 'edit':
            item_index = int(input("Enter an index to edit: "))
            orig_item = items[item_index].strip('\n')

            user_input = input(f"Enter the new item to replace '{orig_item}': ")
            items[item_index] = f"{user_input}\n"
            
            message = f"Item {item_index} '{orig_item}' was changed to '{user_input}'."

        case 'complete':
            item_select = int(input("Enter an index to complete: "))
            removed_item = items.pop(item_select).strip('\n')
            message = f"Item {item_select} '{removed_item}' was removed from the list."

        case 'exit':
            break
    
    # Reduce code redundancy like we did with loading the item list, this time for "add", "edit", or "complete"
    if user_action == "add" or user_action == "edit" or user_action == "complete":
        with open(filename, 'w') as file:
            file.writelines(items)

    print(f"{message}\n") # Print a message to confirm what action was taken

    # The selected action will carry over to the next execution of the for loop
    user_action = input("Type 'Show', 'Add', 'Edit', 'Complete' or 'Exit': ")

print("Closing...\n")