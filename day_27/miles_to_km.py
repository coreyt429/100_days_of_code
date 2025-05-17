import tkinter

# from main import button
WIDGET_PADX = 10
WIDGET_PADY = 10
PADX=20
PADY=20
FONT=('Arial', 12, "normal")

def button_click_handler():
    print("clicked")
    input_string = widget_handles["input"].get()
    try:
        km = 1.609 * int(input_string)
    except ValueError:
        print("invalid input")
        km="invalid"
    widget_handles["result"]["text"] = str(km)


def init_widget(name, widget):
    if widget["type"] == "label":
        new_widget = tkinter.Label(text=widget["text"])
        new_widget.config(font=FONT)
    elif widget["type"] == "button":
        new_widget = tkinter.Button(text=widget["text"], command=widget["command"])
    elif widget["type"] == "entry":
        new_widget = tkinter.Entry(width=widget.get('width', 30))
        new_widget.insert(tkinter.END, string=widget["value"])
    else:
        new_widget = tkinter.Label(text=f"unknown type {widget['type']} for {name}")
    new_widget.grid(column=widget.get('column', 0), row=widget.get('row', 0))
    if widget["type"] not in ["entry"]:
        new_widget.config(padx=WIDGET_PADX, pady=WIDGET_PADY)
    return new_widget

widgets = {
    "input": {"type": "entry", "value": '0', "column": 1, "row": 0, "width": 7},
    "miles": {"type": "label", "text": 'Miles', "column": 2, "row": 0},
    "equal": {"type": "label", "text": 'is equal to', "column": 0, "row": 1},
    "km": {"type": "label", "text": 'Km', "column": 2, "row": 1},
    "result": {"type": "label", "text": '0', "column": 1, "row": 1},
    "button": {"type": "button", "text": 'Calculate', "column": 1, "row": 2, "command": button_click_handler}
}

widget_handles = {}


window = tkinter.Tk()
window.title("Miles to Km")
window.config(padx=PADX, pady=PADY)

for key, value in widgets.items():
    widget_handles[key] = init_widget(key, value)


window.mainloop()