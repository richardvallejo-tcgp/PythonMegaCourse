'''
Day 6 Exercises
'''

'''
Personal Experiment - File Stream Position and Consecutive Read/Write
'''
testfile = "006.01_Day6TestFile.txt"

file = open(testfile, 'w')
file.write('Test File\nContents')
file.close()

file = open(testfile, 'r')
print('1', file.read()) # The first '.read()' method call will read the entire file starting from the beginning
print('2', file.read()) # Subsequent '.read()' calls will start from the stream position, which is now at the end of the file
print('3', file.read(-1)) # Even '.read()' calls with size parameter explicitly set to read the whole file will start from the current stream position
file.close()

file = open(testfile, 'r')
print('4', file.read()) # Closing and re-opening the file will reset the stream position
file.close()

file = open(testfile, 'w')
file.write('\nMore Contents')
file.write('\nEven more')
file.close()

file = open(testfile, 'r')
content = file.read() # Storing the file contents in a variable will allow reading the file contents irrespective of stream position
print('5', file.read()) # '.read()' will start from the end of the file here
print('6', content) # But we can still access the file contents
print('7', content)
print('8', content)
print('9', content)
file.close()

file = open(testfile, 'w')
file.write(content + '\nMore more\nThis is it')
file.close()

file = open(testfile, 'r')
print('10', file.read())
file.close()


'''
Code Experiments
'''
subdir_filename = "006_files/006.0.0_Day6TestFile.txt" # Python uses forward slashes '/' in relative file paths regardless of system (Windows/Mac/Linux)
subdir_file = open(subdir_filename, 'w')
subdir_file.write('Test Subdirectory File Contents')
subdir_file.close()

subdir_file = open(subdir_filename, 'r')
print(subdir_file.read())
subdir_file.close()

documents_filename = r"C:\Users\Public\Documents\Python_Test.txt" # Raw Strings: Avoid backslash '\' characters from causing elements of an absolute Windows path from being interpreted as special characters
documents_file = open(documents_filename, 'w')
documents_file.write('Test Remote File Contents')
documents_file.close()

documents_file = open(documents_filename, 'r')
print(documents_file.read())
documents_file.close()


'''
Bonus
'''
contents = [
    "Contents for "
    "file1.txt", # This string is split across multiple lines in the script but will be interpreted as a single-line string (no backslash required because this is in a list definition)
    "Contents for file2.txt",
    "Contents for file3.txt"
]

filenames = ["file1.txt", "file2.txt", "file3.txt"]

file_prefix = "../006/" \
"006_files" # Because this is a standalone string, a backslash is required to split the definition across multiple lines

print(file_prefix)

for content, filename in zip(contents, filenames):
    path = f"{file_prefix}/{filename}"
    print(f"Writing {content} to {path}")
    file = open(path, 'w')
    file.write(content)
    file.close()    


'''
Coding Exercise 1
'''
essay = open('006_files/essay.txt', 'r')
essay_content = essay.read()
essay_content = essay_content.title()
print(essay_content)


'''
Coding Exercise 2
'''
essay = open('006_files/essay.txt', 'r')
essay_content = essay.read()
print(len(essay_content))


'''
Coding Exercise 3
'''
new_member = input('Add a new member: ')
members = open('006_files/members.txt', 'r')
members_list = members.read()
members.close()

members_list = f"{members_list}{new_member}\n"

members = open('006_files/members.txt', 'w')
members.write(members_list)
members.close()


'''
Coding Exercise 4
'''
filenames = ["exercise4-1.txt", "exercise4-2.txt", "exercise4-3.txt"]
for filename in filenames:
    file = open(f"{file_prefix}/{filename}", 'w')
    file.write('Hello')
    file.close()


'''
Coding Exercise 5
'''
new_files = ["a", "b", "c"]
ext = "txt"
for f in new_files:
    p = f"{file_prefix}/{f}.{ext}"
    file = open(p, 'r')
    print(file.read())


'''
Bug Fixing Exercise 1
'''
file = open("data.txt", 'w')
 
file.write("100.12\n")
file.write("111.23\n")
 
file.close()


'''
Bug Fixing Exercise 2
'''
# file = open("data.txt", 'r')
file = open("data.txt", 'w')
file.write("100.12")
file.close()
