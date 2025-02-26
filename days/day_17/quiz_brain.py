class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self): 
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        result = input(f"Q{self.question_number}.{current_question.text}(true/false): ")
        return result
         


 
        
    def score_calculator(self, answer):
        self.answer = answer.lower()
        print(self.answer)
        print(self.question_list[self.question_number-1].answer.lower)
        if self.answer.lower() == self.question_list[self.question_number-1].answer.lower():
            self.score += 1
            print(f"Correct! Your Score = {self.score}/{self.question_number}")
        else:
            print(f"Incorrect! Your Score = {self.score}/{self.question_number}")    


