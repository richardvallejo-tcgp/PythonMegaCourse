# Define the filename pattern
COURSE_DAY = "15"
FILENAME = f"{(3 - len(COURSE_DAY)) * '0'}{COURSE_DAY}.0_Day{COURSE_DAY}Files/{(3 - len(COURSE_DAY)) * '0'}{COURSE_DAY}.0.1_Day{COURSE_DAY}Data.txt"

INPUT_ERRORS = 0
CONT_PROGRAM = True

# Catch consecutive bad inputs and close the program if we hit a threshold
# Allow the option for error limit to be set on function call with a default parameter value
def input_error_check(input_value, limit=5):
    """Increment consecutive error counter and exit program if limit is reached."""
    global INPUT_ERRORS
    global CONT_PROGRAM
    INPUT_ERRORS += 1
    print(f"There was a problem with the input '{input_value}'.")
    if INPUT_ERRORS >= limit:
        print("Too many consecutive bad inputs encountered. Closing program.")
        CONT_PROGRAM = False
    
    return True


def read_file(filename = FILENAME):
    with open(filename, 'r') as file:
        items = file.readlines()

    return items


def write_file(items, filename = FILENAME):
    with open(filename, 'w') as file:
        file.writelines(items)