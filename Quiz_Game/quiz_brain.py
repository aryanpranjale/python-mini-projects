class QuizBrain:
    def __init__(self, questionlist):
        self.questionlist = questionlist
        self.question_no = 0
        self.score = 0 

    def next_question(self):
        question = self.questionlist[self.question_no]
        print(question.text)
        user_ans = input("is it True or False? : \n").lower().strip()
        options = ["true","t","false","f"]
        if user_ans in options:   
            if user_ans in ["true","t"]:
                user_ans = True
            elif user_ans in ["false","f"]:
                user_ans = False 

            if question.answer== user_ans:
                print("You go it right! ")
                self.score += 1 
            else:
                print("Oops! You got it wrong!")
            self.question_no += 1
        else:
            print("Enter a correct input (T/F)")


    def still_has_question(self):
        total_questions = len(self.questionlist)
        has_question = self.question_no < total_questions
        return has_question
        
    def show_score(self):
        
        print(f"You answered {self.score}/{len(self.questionlist)} correctly")
            
        