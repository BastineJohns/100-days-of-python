from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def question_bank():
    question_bank = []
    for question in question_data:
        question_bank.append(Question(question["text"], question["answer"]))
    return question_bank

ques_bank = question_bank()
Quiz = QuizBrain(ques_bank)
while Quiz.still_has_question():
    answer = Quiz.next_question()
    Quiz.score_calculator(answer)

    
    