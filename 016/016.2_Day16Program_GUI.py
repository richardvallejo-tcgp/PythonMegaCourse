'''
Day 16 Graphical User Interface Program
'''
import functions
import PySimpleGUI as gui

label = gui.Text("Add an item")
input_box = gui.InputText(tooltip="Type a brief description of the item")
add_button = gui.Button("Add")

window = gui.Window("Bop-It Planner", layout=[[label], [input_box, add_button]])
window.read()
window.close()