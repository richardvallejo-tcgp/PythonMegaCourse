'''
Day 9 Program: If Conditional Statements
'''
print("Starting...")

# Define the filename pattern
course_day = "9"
filename = f"{(3 - len(course_day)) * '0'}{course_day}.0_Day{course_day}Files/{(3 - len(course_day)) * '0'}{course_day}.0.1_Day{course_day}Data.txt"

# Avoid repeating the open/read code block multiple times
with open(filename, 'r') as file:
    items = file.readlines() # Create our items list which can be modified and written back to the file periodically

# I want to start each execution by displaying the saved list of items
user_input = "Show"

while True:
    # Define our message to display at the end of the loop
    message = "End of request"
    user_action = user_input.lower().strip() # Enable flexible matching by forcing any input to lowercase and remove whitespace

    if user_action.startswith('show'): # Because the script sets "Show" as the option initially, this will always run first
        print("---")

        # I like this method for removing line breaks because we are performing other operations during the for loop
        for index, item in enumerate(items):
            item = item.strip('\n')
            print(f"{index}-{item}")

        message = "---"

    # There is some code I want to run for multiple conditions (writing to file), so I will nest conditional statements
    elif user_action.startswith('add') or user_action.startswith('edit') or user_action.startswith('complete'):
        # Create a separate conditional block to handle each individual condition as necessary
        if user_action.startswith('add'):
            new_item = user_input[3:].strip()
            items.append(f"{new_item}\n")

            message = f"Item {len(items)-1} '{new_item}' was added to the list."

        elif user_action.startswith('edit'):
            item_index = int(user_input[4:])
            orig_item = items[item_index].strip('\n')

            new_item = input(f"Enter the new item to replace '{orig_item}': ").strip()
            items[item_index] = f"{new_item}\n"

            message = f"Item {item_index} '{orig_item}' was changed to '{new_item}'."

        elif user_action.startswith('complete'):
            item_index = int(user_input[8:])
            removed_item = items.pop(item_index).strip('\n')
            
            message = f"Item {item_index} '{removed_item}' was removed from the list."
      
        # Write to the file at the end of the multi-condition block
        with open(filename, 'w') as file:
              file.writelines(items)

    elif user_action.startswith('exit'):
        break
    
    else:
        message = "Invalid command!"

    print(f"{message}\n") # Print a message to confirm what action was taken

    # The selected action will carry over to the next execution of the for loop
    user_input = input("Type 'Show', 'Add', 'Edit', 'Complete' or 'Exit': ")

print("Closing...\n")