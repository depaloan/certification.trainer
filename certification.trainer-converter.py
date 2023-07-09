#!/usr/bin/env python

import sys
from pathlib import Path

if (len(sys.argv) != 2):
    print("Please provide input TXT file")
    print("Usage: certification.trainer-converter.py MY_CERT.txt") 
    sys.exit(1)

file_path = Path(sys.argv[1])
if (not file_path.is_file()):
    print("File does not exists or user is not allowed to access it")
    print("Usage: certification.trainer-converter.py MY_CERT.txt") 
    sys.exit(1)

begin_answers=0
explaination_string=""

with open(file_path, 'r', encoding='utf-8') as source:
    print('{') 
    print('"questions": [') 
    for line in source:
        if ('-- ' in line and not ('-- explaination: ' in line) ):
            #if ('-- certification_name: ' in line):
            #    certification_name=line.split(': ')
            #    print(certification_name[1])
            #    #"certification_name": "Heavy Metal quiz",
            pass
        else:
            if ( ('Y. ' in line) or ('N. ' in line) ):
                if not(begin_answers==0):
                    print(',')
                print('"' + line.strip() + '"', end = '')
                begin_answers=1
            if ( not ('Y. ' in line) and not ('N. ' in line) and not(len(line) == 1) and not ('-- explaination: ' in line) ):
                print('{')
                print('"question": "' + line.strip() + '",')
                print('"answers": [')
            if ( ('-- explaination: ' in line) ):
                explaination=line.split(': ')
                explaination_string=explaination[1]
            if ( (len(line) == 1) and begin_answers==1):
                print('\n]')
                if (len(explaination_string) > 1):
                    print(',"explaination": "' + explaination_string.strip() + '"')
                    explaination_string=''
                print('},') 
                begin_answers=0
    print(']')
    print('}') 
print(']')
print('}') 