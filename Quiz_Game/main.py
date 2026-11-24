from quiz_brain import QuizBrain as QB
from data import Question_list as Q_list

quiz = QB(Q_list)

while quiz.still_has_question():
    quiz.next_question()

quiz.show_score()