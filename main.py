import Question
import usefulFunctions
import random

total_questions = len(Question.questions)
correct_answers = 0
counter = total_questions
question_explanation = Question.Question("Vuoi visualizzare la spiegazione delle risposte corrette?", "S")
show_every_explanation = usefulFunctions.askQuestion(question_explanation, "S", "N", False, False)

while(counter > 0):
    random_question_index = random.randint(0, counter - 1)
    if(usefulFunctions.askQuestion(Question.questions[random_question_index], "V", "F", True, show_every_explanation)):
        correct_answers += 1
    
    Question.questions.remove(Question.questions[random_question_index])
    counter -= 1


print("Hai risposto correttamente a " + str(correct_answers) + " su " + str(total_questions) + " domande")