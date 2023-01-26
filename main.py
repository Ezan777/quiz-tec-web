import Question
import usefulFunctions
import random

total_questions = len(Question.questions)
correct_answers = 0
counter = total_questions

while(counter > 0):
    random_question_index = random.randint(0, counter - 1)
    if(usefulFunctions.askQuestion(Question.questions[random_question_index])):
        correct_answers += 1
        usefulFunctions.playSound("assets/audio/correct-answer.wav")
    else:
        usefulFunctions.playSound("assets/audio/wrong-answer.wav")
    
    Question.questions.remove(Question.questions[random_question_index])
    counter -= 1


print("Hai risposto correttamente a " + str(correct_answers) + " su " + str(total_questions) + " domande")