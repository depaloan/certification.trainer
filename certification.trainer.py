#!/bin/python3

# TODO: input JSON file should be passed as argument

import json
import os
import random

from rich import print
from rich.console import Console
from rich.prompt import Confirm

console = Console()

with open("certification.trainer.json", "r") as read_content:
    json_questions = json.load(read_content)

    number_available_questions=len(json_questions['questions'])

    i=0

    number_correct_answers=0

    random_available_questions = list(range(number_available_questions))
    random.shuffle(random_available_questions)
    for i in random_available_questions:
        os.system('clear')

        print(json_questions['questions'][i]['question'] +"\n")
        answer_id=1
        correct_answer=[]

        answers_list = json_questions['questions'][i]['answers']
        random.shuffle(answers_list)
        # FIXME: non sono riuscito a inserire le due righe precedenti direttamente nel ciclo FOR
        for answer in answers_list:
            print(str(answer_id) +". " + answer[3:])
            if answer[0] == 'Y':
                correct_answer.append(answer_id)
            answer_id=answer_id+1

        number_of_answers=len(correct_answer)

        inserted_answers_str = input("\nInsert the right answer(s) ["+ str(number_of_answers) +"]: ")
        inserted_answers_str=inserted_answers_str.replace(',', ' ')
        inserted_answers = list(map(int, inserted_answers_str.split(" ")))

        if inserted_answers == correct_answer:
            #print("OK")
            number_correct_answers=number_correct_answers+1
        #else:
            #print("KO")

        #print(inserted_answers)
        #print(correct_answer)

        os.system('clear')
        print(json_questions['questions'][i]['question'])

        answer_id=1
        console.print("")
        for answer in answers_list:
            if ((answer_id in inserted_answers) and (answer_id not in correct_answer)):
                console.print("[red]" + str(answer_id) +". :x: " + answer[3:] + "[/red]")
            elif ((answer_id in inserted_answers) and (answer_id in correct_answer)):
                console.print("[bold green]" + str(answer_id) +". :white_check_mark: " + answer[3:] + "[/bold green]")
            elif ((answer_id not in inserted_answers) and (answer_id in correct_answer)):
                console.print("[bold]" + str(answer_id) +". :white_check_mark: " + answer[3:] + "[/bold]")
            else:
                print(str(answer_id) +". " + answer[3:])
            answer_id=answer_id+1

        i=i+1

        Confirm.ask("\nGo to next question")
        # TODO: gestire l'opzione N
        print("\n\n\n")

os.system('clear')
print("number of total questions: " + str(number_available_questions))
print("number of correct answers: " + str(number_correct_answers))
print("% of correct answers: " + str(round(((number_correct_answers/number_available_questions)*100),2) ))

