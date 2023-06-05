'''
Day 16 Exercises
'''
import exercises
import PySimpleGUI as psg
folder = "016.0_Day16Files"
bonus = "016.0.2_Day16BonusData.txt"

'''
Code Experiments
'''
label = psg.Text("Add an item")
input_box = psg.InputText(tooltip="Type a brief description of the item")
add_button = psg.Button("Add")

# window = psg.Window("Bop-It Planner", layout=[label, input_box, add_button]) # This results in an error because layout needs to be a list of lists
# window = psg.Window("Bop-It Planner", layout=[["Text"], [input_box, add_button]]) # This also results in an error because all list items need to be instances of a PySimpleGUI class
window = psg.Window("Bop-It Planner", layout=[[label], [input_box], [add_button]]) # This generates one element per row
window.read()
window.close()


'''
Bonus
'''
file_label = psg.Text("Select files to compress")
file_input = psg.Input()
file_button = psg.FileBrowse("Browse Files")

folder_label = psg.Text("Select destination folder")
folder_input = psg.Input()
folder_button = psg.FolderBrowse("Browse Folders")

compress_button = psg.Button("Compress")

window = psg.Window("Compress Files",
                    layout=[[file_label, file_input, file_button],
                            [folder_label, folder_input, folder_button],
                            [compress_button]])

window.read()
window.close()


'''
Coding Exercise 1
'''
feet_label = psg.Text("Enter feet:")
feet_input = psg.Input()
inch_label = psg.Text("Enter inches:")
inch_input = psg.Input()
conv_button = psg.Button("Convert")
conv_layout = [[feet_label, feet_input],
               [inch_label, inch_input],
               [conv_button]]
conv_window = psg.Window("Converter", layout=conv_layout)

conv_window.read()
conv_window.close()


'''
Bug Fixing Exercise 1
'''
label = psg.Text("What are dolphins?")
option1 = psg.Radio("Amphibians", group_id="question1")
option2 = psg.Radio("Fish", group_id="question1")
option3 = psg.Radio("Mammals", group_id="question1")
option4 = psg.Radio("Birds", group_id="question1")
 
window = psg.Window("File Compressor",
                   layout=[[label],
                           # [option1, option2, option3, option4],
                           [option1],
                           [option2],
                           [option3],
                           [option4]
                           ])
 
window.read()
window.close()
