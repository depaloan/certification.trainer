#!/bin/python3

import json
import os
import random
import sys
from pathlib import Path

from rich import print
from rich.console import Console
from rich.prompt import Confirm

console = Console()

if (len(sys.argv) != 2):
    print("Please provide JSON file")
    print("Usage: certification.trainer.py MY_CERT.json") 
    sys.exit(1)


file_path = Path(sys.argv[1])
if (not file_path.is_file()):
    print("File does not exists or user is not allowed to access it")
    print("Usage: certification.trainer.py MY_CERT.json") 
    sys.exit(1)

def print_statics():
    os.system('clear')
    print("number of total questions: \t" + str(number_available_questions))
    print("number of answered questions: \t" + str(number_of_answered_questions))
    print("number of correct answers: \t" + str(number_correct_answers))
    print("% of correct answers: \t\t" + str(round(((number_correct_answers/number_of_answered_questions)*100),2) ))

with open(file_path, "r") as read_content:
    json_questions = json.load(read_content)

    number_available_questions=len(json_questions['questions'])

    os.system('clear')
    console.print("[green bold]" +  json_questions['certification_name'] + "[/green bold] ([blue bold]" +  json_questions['certification_code'] + "[/blue bold])\n")
    console.print("[italic]" +  json_questions['certification_description'] + "[/italic]\n")
    console.print("Number of available questions: [bold]" + str(number_available_questions) + "[/bold]")
    ready_to_go = Confirm.ask("\nAre you ready to start?")

    if (not ready_to_go):
        sys.exit(0)

    i=0

    explaination=""
    number_correct_answers=0
    number_of_answered_questions=0

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

        # look for an "explaination" item
        try:
            explaination=json_questions['questions'][i]['explaination']
        except:
            # if not present, don't do anything
            pass
        else:
            # if present, print it 
            console.print("\n[italic]" + json_questions['questions'][i]['explaination'] + "[italic]")

        i=i+1
        number_of_answered_questions=number_of_answered_questions+1

        proceed_next_question = Confirm.ask("\nGo to next question?")
        if (not proceed_next_question):
            print_statics()
            sys.exit(0)
        print("\n\n\n")

print_statics()