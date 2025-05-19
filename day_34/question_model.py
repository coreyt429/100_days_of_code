"""
This file contains the Question class
"""

import html


class Question:
    """
    Data structure to hold the question and answer.
    """

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

    def __str__(self):
        """
        Returns the string representation of the Question object.
        """
        return f"{html.unescape(self.text)}"

    def __repr__(self):
        """
        Returns the string representation of the Question object.
        """
        return f"Question(text={self.text}, answer={self.answer})"
