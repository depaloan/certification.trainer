#!/usr/bin/env python

begin_answers=0

with open('file.txt', 'r', encoding='utf-8') as source:
    for line in source:
        #print(line.strip())
        if ( ('Y. ' in line) or ('N. ' in line) ):
            if not(begin_answers==0):
                print(',')
            print('"' + line.strip() + '"', end = '')
            begin_answers=1
        if ( not ('Y. ' in line) and not ('N. ' in line) and not(len(line) == 1) ):
            print('{')
            print('"question": "' + line.strip() + '",')
            print('"answers": [')
        if ( (len(line) == 1) and begin_answers==1):
            print(']')
            print('},') 
            begin_answers=0
    print(']')
    print('}') 
