'''
Day 14 Program: Modules and Import
'''
import functions

print("Starting...")
input_text = "Type 'Show', 'Add', 'Edit', 'Complete' or 'Exit': "

# View the docstring for the custom function
help(functions.input_error_check)

items = functions.read_file()

# I want to start each execution by displaying the saved list of items
user_input = "Show"

while functions.CONT_PROGRAM:
    # Define our message to display at the end of the loop
    message = "End of request"
    user_action = user_input.lower().strip() # Enable flexible matching by forcing any input to lowercase and remove whitespace
    input_error = False

    # Provide a quick exit when requested, and avoid running any code in the 'finally' block below
    if user_action.startswith('exit'):
        break
    
    else:
        try:
            if user_action.startswith('show'): # Because the script sets "Show" as the option initially, this will always run first
                print("---")

                if len(items) > 0:
                    # I like this method for removing line breaks because we are performing other operations during the for loop
                    for index, item in enumerate(items):
                        item = item.strip('\n')
                        print(f"{index}-{item}")
                else:
                    print("No items in list. Type 'add' followed by an item description to add your first item!")

                message = "---"

            # There is some code I want to run for multiple conditions (writing to file), so I will nest conditional statements
            elif user_action.startswith('add') or user_action.startswith('edit') or user_action.startswith('complete'):
                # Create a separate conditional block to handle each individual condition as necessary
                if user_action.startswith('add'):
                    new_item = user_input[3:].strip()
                    
                    # Enforce item string length greater than zero
                    if len(new_item) > 0:
                        items.append(f"{new_item}\n")
                        message = f"Item {len(items)-1} '{new_item}' was added to the list."

                    else:
                        message = f"Items cannot be blank."
                        input_error = functions.input_error_check(new_item)

                elif user_action.startswith('edit'):
                    item_index = int(user_input[4:])
                    orig_item = items[item_index].strip('\n')

                    new_item = input(f"Enter the new item to replace '{orig_item}': ").strip()

                    # Enforce item string length greater than zero
                    if len(new_item) > 0:
                        items[item_index] = f"{new_item}\n"
                        message = f"Item {item_index} '{orig_item}' was changed to '{new_item}'."
                    
                    else:
                        message = f"Items cannot be blank."
                        input_error = functions.input_error_check(new_item)

                elif user_action.startswith('complete'):
                    item_index = int(user_input[8:])
                    removed_item = items.pop(item_index).strip('\n')
                    
                    message = f"Item {item_index} '{removed_item}' was removed from the list."

                functions.write_file(items)

            else:
                message = "Invalid command!"
                input_error = functions.input_error_check(user_input)

        except ValueError:
            message = "The selected command expects an integer value."
            input_error = functions.input_error_check(user_input)
            continue
        
        except IndexError:
            message = "The selected index is out of range."
            input_error = functions.input_error_check(user_input)
            continue

        # The 'finally' condition allows us to run code regardless of whether there was an error or not, but it also always runs before a 'break' above will exit the loop
        finally:
            print(f"{message}\n") # Print a message to confirm what action was taken

            # Reset input error counter on successful input
            if not input_error:
                functions.INPUT_ERRORS = 0

            # If the program will continue, ask for a command
            if functions.CONT_PROGRAM:
                # The selected action will carry over to the next execution of the for loop
                # This runs in the 'finally' block so that input is requested whether good or bad input was given previously
                user_input = input(input_text)

print("Closing...\n")