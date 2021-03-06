from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for content in question_data:
    question_text = content['question']
    question_answer = content['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz.next_question()
