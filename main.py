from question_model import Question
from data import question_data

question_bank = []

for content in question_data:
    question_text = content['text']
    question_answer = content['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


