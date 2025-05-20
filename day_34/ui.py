"""
Quiz UI Module
"""

from tkinter import Tk, Canvas, Button, Label, PhotoImage

THEME_COLOR = "#375362"


class QuizInterface:
    """
    A class to create the UI for the quiz application.
    """

    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.quiz.next_question()
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.widgets = {}
        self.widgets["canvas"] = Canvas(width=300, height=250, bg="white")
        self.question_text = self.widgets["canvas"].create_text(
            150,
            125,
            text=self.quiz.question_text,
            width=280,
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.widgets["canvas"].grid(row=1, column=0, columnspan=2, pady=50)
        self.widgets["score_label"] = Label(
            text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white"
        )
        self.widgets["score_label"].grid(row=0, column=1)
        self.widgets["true_image"] = PhotoImage(file="images/true.png")
        self.widgets["false_image"] = PhotoImage(file="images/false.png")
        self.widgets["true_button"] = Button(
            image=self.widgets["true_image"],
            highlightthickness=0,
            command=self.true_pressed,
        )
        self.widgets["true_button"].grid(row=2, column=0)
        self.widgets["false_button"] = Button(
            image=self.widgets["false_image"],
            highlightthickness=0,
            command=self.false_pressed,
        )
        self.widgets["false_button"].grid(row=2, column=1)
        self.window.mainloop()

    def next_question(self):
        """
        Displays the next question in the quiz.
        """
        self.widgets["canvas"].config(bg="white")
        if self.quiz.still_has_questions():
            self.quiz.next_question()
            self.widgets["score_label"].config(text=f"Score: {self.quiz.score}")
            self.widgets["canvas"].itemconfig(
                self.question_text, text=self.quiz.question_text
            )
        else:
            self.widgets["canvas"].itemconfig(
                self.question_text, text="You've completed the quiz"
            )
            self.widgets["true_button"].config(state="disabled")
            self.widgets["false_button"].config(state="disabled")
            self.widgets["score_label"].config(
                text=f"Score: {self.quiz.score}/{self.quiz.question_number}"
            )

    def true_pressed(self):
        """
        Checks if the answer is true and updates the score.
        """
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        """
        Checks if the answer is false and updates the score.
        """
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        """
        Provides feedback to the user based on their answer.
        """
        if is_right:
            self.widgets["canvas"].config(bg="green")
        else:
            self.widgets["canvas"].config(bg="red")
        self.window.after(1000, self.next_question)
