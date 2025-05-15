import tkinter as tk
from fileinput import filename

import pandas as pd
from random import shuffle

from pandas.core.interchange.dataframe_protocol import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

after_handle = None
def default_cmd(*args):
    print(f"default_cmd({args})")

def right_clicked(*args):
    words['correct'].append(words['current'].pop(0))
    save_progress()
    display_card()

def wrong_clicked(*args):
    words['incorrect'].append(words['current'].pop(0))
    display_card()

def save_progress():
    to_learn = [todo for todo in words['current']]
    to_learn.extend([todo for todo in words['incorrect']])
    df = pd.DataFrame(data=to_learn)
    df.to_csv("data/french_words_to_learn.csv", index=False)

def load_word_data():
    new_words = {
        "all": [],
        "correct": [],
        "incorrect": []
    }
    try:
        data = pd.read_csv("data/french_words_to_learn.csv")
    except FileNotFoundError:
        data = pd.read_csv("data/french_words.csv")
    except pd.errors.EmptyDataError:
        data = pd.read_csv("data/french_words.csv")
    new_words['all'] = data.to_dict(orient="records")
    # for idx, series in data.iterrows():
    #     new_words['all'].append((series['French'], series['English']))
    return new_words

def reset():
    words['incorrect'] = []
    next_round()

def next_round():
    source = words['all']
    if words['incorrect']:
        source = words['incorrect']
        words['incorrect'] = []
        print(f"{len(source)} incorrect cards loaded")
    new_cards = [word_card for word_card in source]
    shuffle(new_cards)
    words['current'] = new_cards

def flip_card():
    card.itemconfig(card_image, image=card_back)
    card.itemconfig(card_language, text='English', fill="white")
    card.itemconfig(card_word, text=words['current'][0]['English'], fill="white")

def display_card():
    global after_handle
    if not after_handle is None:
        window.after_cancel(after_handle)
    if not words['current']:
        next_round()
    card.itemconfig(card_image, image=card_front)
    card.itemconfig(card_language, text='French', fill="black")
    card.itemconfig(card_word, text=words['current'][0]['French'], fill="black")
    after_handle = window.after(3000, flip_card)

    # card.create_text(400, 150, text="French", font=LANGUAGE_FONT)
    # card.create_text(400, 263, text=words['current'][0][0], font=WORD_FONT)
    # card.create_text(400, 263, text=words['current'][0]['French'], font=WORD_FONT)

#################### UI ####################
window = tk.Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR)
# window.config(height=626, width=900)
window.config(padx=50, pady=50)

card = tk.Canvas(bg=BACKGROUND_COLOR, height=526, width=800, highlightthickness=0)
card.grid(row=0, column=0, columnspan=2)

card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")
card_image = card.create_image((400, 263), image=card_front)
card_language = card.create_text(400, 150, text="Language", font=LANGUAGE_FONT)
card_word = card.create_text(400, 263, text="Word", font=WORD_FONT)



buttons_definitions = {
    "right": {
        "image" : "images/right.png",
        "command": right_clicked,
        "placement": (1, 1, 1)
    },
    "wrong": {
        "image" : "images/wrong.png",
        "command": wrong_clicked,
        "placement": (1, 0, 1)
    }
}

buttons = {}
for button_id, button_def in buttons_definitions.items():
    new_button = {
        "image": tk.PhotoImage(file=button_def["image"])
    }
    new_button["button"] = tk.Button(image=new_button["image"], highlightthickness=0, command=button_def["command"])
    row, col, col_span = button_def["placement"]
    new_button["button"].grid(row=row, column=col, columnspan=col_span)
    buttons[button_id] = new_button

#################### DATA ####################
words = load_word_data()
next_round()
display_card()

window.mainloop()