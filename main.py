from quiz_logic import QuizBrain
from quiz_gui import QuizInterface
from random import shuffle
import html
import requests
class Ques:
    def __init__(self, question: str, correct_answer: str, choices: list):
        self.question_text = question
        self.correct_answer = correct_answer
        self.choices = choices
parameters = {
    "amount": 10,
    "type": "multiple"

}
response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type="
                            "multiple",
                        params=parameters)
question_info = response.json()["results"]
question_bank = []
for question in question_info:
    choices = []
    question_text = html.unescape(question["question"])
    correct_answer = html.unescape(question["correct_answer"])
    incorrect_answers = question["incorrect_answers"]
    for ans in incorrect_answers:
        choices.append(html.unescape(ans))
    choices.append(correct_answer)
    shuffle(choices)
    new_question = Ques(question_text, correct_answer, choices)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
print(f"Your final score is : {quiz.score}/{quiz.question_no}")