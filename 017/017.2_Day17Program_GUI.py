'''
Day 17 Graphical User Interface Program
'''
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

window = gui.Window("Bop-It Planner",
                    layout=[[label], [input_box, add_button, clear_button], [item_list, edit_button, refresh_button], [exit_button]],
                    font=('Helvetica', 14))

while True:
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