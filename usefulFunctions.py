import os
import platform

def parseAnswer(answer):
    return answer.upper()

def askQuestion(question):
    answered = False
    while not answered:
        answer = input(question.question + " [V/F] ")
        answer = parseAnswer(answer)
        if answer is None:
            print("Risposta non valida")
        else:
            answered = True
            if question.check_answer(answer):
                print("Risposta corretta :)")
                printSeparator()
                return True
            else:
                print("Risposta errata :( La risposta era " + question.answer)
                printSeparator()
                return False

def printSeparator():
    print("=" * os.get_terminal_size().columns)