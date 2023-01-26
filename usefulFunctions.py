import os
import platform

def parseAnswer(answer, positive_answer = "V", negative_answer = "F"):
    answer = answer.upper()
    if answer == positive_answer.upper():
        return answer
    elif answer == negative_answer.upper():
        return answer
    else:
        return None

def askQuestion(question, positive_answer = "V", negative_answer = "F", show_correct_answer = True, show_every_explanation = False):
    answered = False
    while not answered:
        answer = input(question.question + f" [{positive_answer}/{negative_answer}] ")
        answer = parseAnswer(answer, positive_answer, negative_answer)
        if answer is None:
            print("Risposta non valida")
        else:
            answered = True
            if show_correct_answer:
                if question.check_answer(answer):
                    print("Risposta corretta :)")
                    if show_every_explanation:
                        printSeparator("+")
                        print("\n"+question.explanation+"\n")
                        printSeparator("+")
                    else:
                        printSeparator("=")

                    return True
                else:
                    print("Risposta errata :( La risposta era " + question.answer)
                    printSeparator("+")
                    print("\n"+question.explanation+"\n")
                    printSeparator("+")
                    return False
            else:
                return question.check_answer(answer)

def printSeparator(char):
    if(len(char) > 1): char = char[0]
    print(char * os.get_terminal_size().columns)