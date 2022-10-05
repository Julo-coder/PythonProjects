from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_q = Question(question["question"], question["correct_answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
else:
    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")


