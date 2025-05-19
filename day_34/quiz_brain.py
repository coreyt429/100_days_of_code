"""
This file contains the QuizInterface class
which is responsible for creating the GUI for the quiz application.
"""


class QuizBrain:
    """
    A class to manage the quiz logic and keep track of the score.
    """

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.question_text = None

    def still_has_questions(self):
        """
        Method to check if there are more questions left in the quiz.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Method to get the next question from the question list."""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.question_text = f"Q. {self.question_number}: {str(self.current_question)}"

    def check_answer(self, user_answer: str) -> bool:
        """
        Method to check if the user's answer is correct.
        """
        correct_answer = self.current_question.answer
        if user_answer[0].lower() == correct_answer[0].lower():
            self.score += 1
            return True
        return False
