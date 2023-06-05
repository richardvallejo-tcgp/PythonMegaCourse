'''
Day 17 Exercises
'''
import exercises
import PySimpleGUI as psg
folder = "017.0_Day17Files"
bonus = "017.0.2_Day17BonusData.txt"


'''
Code Experiments
'''
run_test = input("Run Test Program? Enter 'yes' to run: ")
while run_test == "yes":
    user_input = input("Enter Break or Exit: ")
    match user_input:
        case "Break":
            # Break out of the While loop and continue
            break
        case "Exit":
            # Exit program entirely
            exit()

print("Continuing program")

import functions
import PySimpleGUI as gui

items = functions.read_file()

label = gui.Text("Add an item")
input_box = gui.InputText(tooltip="Type a brief description of the item", key="item")
add_button = gui.Button("Add")
clear_button = gui.Button("Clear")
item_list = gui.Listbox(values=items, key="item_select",
                        enable_events=True, size=[45, 10])
edit_button = gui.Button("Edit")
refresh_button = gui.Button("Refresh")
exit_button = gui.Button("Exit")

# Define an intermediate variable for layout
layout = [[label],
          [input_box, add_button, clear_button],
          [item_list, edit_button, refresh_button],
          [exit_button]]

# Use the intermediate variable when defining the Window instance
window = gui.Window("Bop-It Planner",
                    layout=layout,
                    font=('Helvetica', 14))

run_todo = input("Run To-Do List Program? Enter 'yes' to run: ")
while run_todo == "yes":
    event, values = window.read()
    print(event)
    print(values)
    print(items)
    match event:
        case "Add":
            items.append(f"{values['item']}\n")
            functions.write_file(items)
            window['item'].update(value="")
            window['item_select'].update(values=items)
        case "Clear":
            window['item'].update(value="")
        case "Refresh":
            window['item_select'].update(values=items, set_to_index=[])
        case "item_select":
            window['item'].update(value=values['item_select'][0])
        case "Edit":
            if len(values['item_select']) > 0:
                print(values['item_select'][0])
                index = items.index(values['item_select'][0])
                items[index] = f"{values['item']}\n"
                functions.write_file(items)
            window['item'].update(value="")
            window['item_select'].update(values=items)
        case "Exit" | gui.WIN_CLOSED:
            break


window.close()


'''
Bonus
'''
from exercises import make_archive

file_label = psg.Text("Select files to compress")
file_input = psg.Input(key="files", enable_events=True)
file_button = psg.FilesBrowse("Browse Files")

folder_label = psg.Text("Select destination folder")
folder_input = psg.Input(key="folder", enable_events=True)
folder_button = psg.FolderBrowse("Browse Folders")

compress_button = psg.Button("Compress", key="compress")
output_message = psg.Text(key="results")

window = psg.Window("Compress Files",
                    layout=[[file_label, file_input, file_button],
                            [folder_label, folder_input, folder_button],
                            [compress_button, output_message]])

run_compression = input("Run Compression Program? Enter 'yes' to run: ")
while run_compression == "yes":
    event, values = window.read()
    print(event, values)
    files = values['files'].split(";")
    folder = values['folder']
    make_archive(files, folder)
    if event == "compress":
        window["results"].update(value="Compression complete!")
    else:
        window["results"].update(value="")

window.close()


'''
Coding Exercise 1
'''
# May need to install converters using pip
import converters as conv
# from converters import convert

feet_label = psg.Text("Feet:")
feet_input = psg.Input(key="feet")

inch_label = psg.Text("Inches:")
inch_input = psg.Input(key="inch")

conv_button = psg.Button("Convert")
conv_results = psg.Text(key="results")

conv_layout = [[feet_label, feet_input],
          [inch_label, inch_input],
          [conv_button, conv_results]]

window = psg.Window("Measurement Converter", layout=conv_layout)

run_converter = input("Run Converter program? Enter 'yes' to run: ")

while run_converter == "yes":
    event, values = window.read()
    feet = float(values['feet'])
    inch = float(values['inch']) + (feet * 12)
    meters = inch * .0254
    # result = convert()
    window['results'].update(value=f"{meters} m")

window.close()


'''
Bug-Fixing Exercise 1
'''

def km_to_miles(km):
    return km / 1.6
 
 
label = psg.Text("Kilometers: ")
input_box = psg.InputText(tooltip="Enter todo", key="kms")
miles_button = psg.Button("Convert")
 
output = psg.Text(key="output")

window = psg.Window('Km to Miles Converter',
                   layout=[[label, input_box], [miles_button, output]],
                   font=('Helvetica', 20))
 
run_bugfix = input("Run Bug Fix program? Enter 'yes' to run: ")
while run_bugfix == "yes":
    event, values = window.read()
    match event:
        case "Convert":
            # km = values["kms"]
            km = float(values["kms"])
            result = km_to_miles(km)
            window['output'].update(value=result)
        case psg.WIN_CLOSED:
            break
 
window.close()