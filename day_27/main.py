import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500,300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="test label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

def button_clicked():
    # val = int(my_label_2["text"])
    # val+=1
    # my_label_2["text"] = str(val)
    new_string = my_input.get()
    my_label['text'] = my_input.get()
    print(new_string)
    # print(multi_line.get("1.0", tkinter.END))

button = tkinter.Button(text="Push", command=button_clicked)
button.grid(column=1, row=1)

my_input = tkinter.Entry()
my_input.grid(column=3, row=2)

# my_label_2 = tkinter.Label(text="0", font=("Arial", 24, "bold"))
# my_label_2.grid(column=3, row=3)

button_2 = tkinter.Button(text="Click", command=button_clicked)
button_2.grid(column=2, row=0)

# multi_line = tkinter.Text()
# multi_line.grid()


window.mainloop()