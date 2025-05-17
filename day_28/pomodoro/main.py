
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✓"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
PAD_X=0
PAD_Y=0
TEST=False

DELAY=1000
if TEST:
    DELAY = 2

TIMERS = (WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN)
timer = {"state": 0, "counter": 0, "reps": 1, "progress": "", "handle": ""}
labels = {
    WORK_MIN: "Work",
    SHORT_BREAK_MIN: "Break",
    LONG_BREAK_MIN: "Break"
}

colors = {
    WORK_MIN: GREEN,
    SHORT_BREAK_MIN: PINK,
    LONG_BREAK_MIN: RED
}

# ---------------------------- TIMER RESET ------------------------------- # 

def timer_reset():
    timer["state"] = 0
    timer["counter"] = 0
    timer["progress"] = ""
    timer["reps"] = 1
    window.after_cancel(timer['handle'])
    label_title.config(text="Timer", fg=GREEN)
    label_state.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def display_timer():
    seconds = timer["counter"] % 60
    minutes = math.floor(timer["counter"] / 60)
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")

def start_timer(state=0):
    timer["state"] = state
    timer["counter"] = 60*TIMERS[timer["state"]]
    label_title.config(text=labels[TIMERS[timer["state"]]], fg=colors[TIMERS[timer["state"]]])
    display_timer()
    count_down(decrement=False)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(decrement=True):
    if decrement:
        timer["counter"] -= 1
    display_timer()
    if timer["counter"] > 0:
        timer["handle"] = window.after(DELAY, count_down, True)
    else:
        timer['reps'] += 1
        timer['state'] = 0
        print(f"reps: {timer['reps']}")
        if timer['reps'] % 8 == 0:
            timer['state'] = 2
        elif timer['reps'] % 2 == 0:
            timer['state'] = 1
        if timer['reps'] % 2 == 0:
            timer['progress'] += CHECK_MARK
            label_state.config(text=timer["progress"])

        start_timer(timer['state'])

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.configure(padx=100, pady=50, bg=YELLOW)

# title
label_title = Label(window, text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
label_title.grid(row=0, column=1, padx=PAD_X, pady=PAD_Y)

# label result
label_state = Label(window, text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
label_state.grid(row=3, column=1, padx=PAD_X, pady=PAD_Y)

# start button
start_button = Button(
   window,
   text="Start",
   command=start_timer
)
start_button.grid(row=2, column=0, padx=PAD_X, pady=PAD_Y)

# reset button
reset_button = Button(
   window,
   text="Reset",
   command=timer_reset
)
reset_button.grid(row=2, column=2, padx=PAD_X, pady=PAD_Y)


# tomato canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1, padx=PAD_X, pady=PAD_Y)



window.mainloop()