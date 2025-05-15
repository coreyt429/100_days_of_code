import tkinter
import tkinter.messagebox as messagebox
import json
from random import shuffle, randint, choice
import string
import pyperclip

passwords = {}
PASSWORD_FILE='data.json'
# from PIL import Image, ImageTk
BUTTON_FONT = ("Helvetica", 10, "normal")
# ---------------------------- SEARCH ----------- ------------------------------- #

def search_passwords(*args):
    search_string = entries['website']['string'].get()
    message = ""
    for password_id, password in passwords.items():
        if search_string.lower() in password_id.lower():
            message = ""
            for field in ['website', 'email', 'password']:
                message += f"{field.title()}: {password[field]}\n"
    if message:
        messagebox.showinfo("Password found", message)
    else:
        messagebox.showinfo("Password not found", f"No password found for {entries['website']['string'].get()}")


# def on_change(*args):
#     search_string = entries['website']['string'].get()
#     for password_id, password in passwords.items():
#         if search_string in password_id:
#             for entry_id in ['website', 'email', 'password']:
#                 entries[entry_id]['string'].set(password[entry_id])


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_password(length=20):
    # define charsets to use
    charsets = (
        string.ascii_letters,
        string.digits,
        ('!', '#', '$', '%', '&', '(', ')', '*', '+')
    )
    # define count for each charset
    char_counts = (
        randint(8, 10),
        randint(2, 4),
        randint(2, 4)
    )
    password_list = []
    for idx, charset in enumerate(charsets):
        password_list.extend(
            [choice(charset) for _ in range(char_counts[idx])]
        )
    shuffle(password_list)
    return ''.join(password_list)

def password_generator():
    password_string = entries['password']['string']
    password_string.set(random_password())
    pyperclip.copy(password_string.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def load_passwords():
    global passwords
    try:
        with open(PASSWORD_FILE) as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}

def save_password():
    current_password = {}
    for field in ["website", "email", "password"]:
        current_password[field] = entries[field]['string'].get()
        # check value, let's not save empty strings
        if current_password[field] == '':
            messagebox.showerror("Oops", f"{field.title()} is empty:\n\nPlease make sure you haven't left any fields empty")
            return
    key = f"{current_password['website']}:{current_password['email']}"
    is_ok = messagebox.askokcancel(
        title=current_password['website'],
        message=f"These are the details entered: \nEmail: {current_password['email']} \nPassword: {current_password['password']} \n Is it okay to save?"
    )
    if is_ok:
        # save the password in memory
        passwords[key] = current_password
        # write to file
        with open(PASSWORD_FILE, 'w') as password_file:
            json.dump(passwords, password_file)
        # clear inputs
        for field in ["website", "email", "password"]:
            entries[field]['string'].set('')
        return


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg='white')
canvas = tkinter.Canvas(window, width=200, height=200, bg='white')
# # Resize the image using Pillow
# original_image = Image.open("logo.png")
# resized_image = original_image.resize((200, 200), Image.LANCZOS)
image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)  # Adjusting to the center of the canvas
canvas.config(highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)  # Use grid layout for precise placement

entry_definitions = {
    "website": {
        "label": {
            "text": "Website:",
            "placement": (1,0,1)
        },
        "entry":{
            "width": 21,
            "placement": (1,1,1)
        }
    },
    "email": {
        "label": {
            "text": "Email/Username:",
            "placement": (2,0,1)
        },
        "entry":{
            "width": 42,
            "placement": (2,1,2)
        }
    },
    "password": {
        "label": {
            "text": "Password:",
            "placement": (3,0,1)
        },
        "entry":{
            "width": 21,
            "placement": (3,1,1)
        }
    },
}

button_definitions = {
    "generate":
        {
            "label": "Generate Password",
            "placement": (3,2,1),
            "width": 14,
            "command": password_generator
        },
    "save":
        {
            "label": "Add",
            "placement": (4,1,2),
            "width": 30,
            "command": save_password
        },
    "search":
        {
            "label": "Search",
            "placement": (1,2,1),
            "width": 14,
            "command": search_passwords
        },
}

entries = {}
for entry_id, entry in entry_definitions.items():
    new_string_var = tkinter.StringVar()
    new_entry = {
        "label": tkinter.Label(text=entry["label"]["text"], bg="white"),
        "string": new_string_var,
        "entry": tkinter.Entry(window, textvariable=new_string_var, width=entry["entry"]["width"])
    }
    for item in ["label", "entry"]:
        widget = new_entry[item]
        widget.grid(
            row=entry[item]['placement'][0],
            column=entry[item]['placement'][1],
            columnspan=entry[item]['placement'][2]
        )
    entries[entry_id] = new_entry
# for entry_id in ['website', 'email']:
#     var = entries[entry_id]['string']
#     var.trace_add("write", on_change)

buttons = {}
for button_id, button in button_definitions.items():
    new_button = tkinter.Button(text=button['label'], width=button['width'], command=button['command'], font=BUTTON_FONT)
    new_button.grid(
        row=button['placement'][0],
        column=button['placement'][1],
        columnspan=button['placement'][2]
    )
    buttons[button_id] = new_button

entries['website']['entry'].focus()
entries['email']['entry'].insert(0, 'coreyt@coreyt.com')
load_passwords()
print(passwords)
window.mainloop()