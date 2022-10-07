#!/usr/bin/env python3

#Conventions

#! camelCase for functions and methods
#! snake_case for variables

# Imports

import pprint # Allows for pretty printing of dictionaries
import argparse
import random
from collections import namedtuple
import readchar
import getch #alternative to input() which doesn't require the enter key stroke
import time

import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)

#Global Variables

input_tuple=namedtuple('input_tuple',['l_s','l_t','t']) # letter_shown,letter_typed,time

#Functions

def modoCount(threshold):
    print('The test will begin shortly, ending after pressing ' + str(threshold) + ' letters.')
    print('Press any key to begin the test!')
    getch.getch() # See line 13
    #_ = readchar.readchar()
    
    # After pressing a key, theres a 3 second countdown before the test starts for the user to prepare.
    for i in range(1,4):
        print('The test will start in '+ str(4-i) +' seconds.')
        time.sleep(1)
    
    print('')
    
    inputs=[]
    
    #? Should we store typed letter/shown letter as ASCII code or Unicode?
    #! Right now its returning as ASCII codes
    # TODO Add colorama here

    time_b4_exec=time.time()

    for i in range(1,threshold+1):
        correct_leter = random.randint(97,122)  # ASCII code
        time_b4 = time.time()
        print("Type letter " + chr(correct_leter))
        typed_letter = ord(readchar.readchar()) #readchar returns a string/char, and ord() converts it to ASCII 
        time_after = time.time()
        print('     You typed letter ' + chr(typed_letter))
        duration = time_after - time_b4
        
        # Here all the parameters are computed, now need to store them
        input=input_tuple(l_s = correct_leter,l_t = typed_letter, t = duration)
        # Now the tuple resulting from a single keypress should be stored to later be returned
        inputs.append(input)
        
    # print(inputs)

    return inputs, time_b4_exec

    

    


def modoTimed(threshold):
    print('The test will begin shortly, ending after ' + str(threshold) + ' seconds.')
    print('Press any key to begin the test')
    getch.getch() # See line 13 

    # After pressing a key, theres a 3 second countdown before the test starts for the user to prepare.
    for i in range(1,4):
        print('The test will start in '+ str(4-i) +' seconds.')
        time.sleep(1)

    print('')
    # TODO Yet to implement
    # return timed_inputs

def buildDict(inputs, abs_b4_time):  # inputs = list of namedTuples
    dict_keys = ['n_hits','n_types','accuracy','test_duration','test_start','test_start','type_avg_dur','hit_avg_dur','miss_avg_dur','types']
    stat_dict = dict.fromkeys(dict_keys,0) # keys = list , values = 0
    #! Any namedTuple can be accessed either by x[1] or x.argument
    total_hit_time = 0
    total_miss_time = 0
    
    for i in range(0,len(inputs)): #len() returns nº of elements of the list, which index starts at 0
        #//current_tuple = inputs[i]
        #* Number of hits
        if inputs[i].l_t == inputs[i].l_s:
            stat_dict['n_hits'] += 1
            #* Total hit time, yet to be divided by the number of hits
            total_hit_time += inputs[i].t
        else:
            total_miss_time += inputs[i].t 
        #* Test duration
        stat_dict['test_duration'] += inputs[i].t


    #Number of misses - *only used in mid calculations*
    n_misses = stat_dict['n_types'] - stat_dict['n_hits']

    #* Number of types
    stat_dict['n_types'] = len(inputs)

    #* Accuracy
    stat_dict['accuracy'] = stat_dict['n_hits'] / stat_dict['n_types']

    #* Test start
    stat_dict['test_start'] = time.ctime(abs_b4_time)

    #* Test end
    stat_dict['test_end'] = time.ctime(abs_b4_time + stat_dict['test_duration'])

    #* Average type time 
    # The test time won't ever be 0 seconds, so there ain't a problem by dividing by the time
    avg_type_time = stat_dict['test_duration'] / len(inputs) #!Trick to assure only 3 decimal points
    stat_dict['type_avg_dur'] = str(avg_type_time) + 's'

    print(len(inputs))
    #* Average miss time
    #! Here we have to watch out in case total_miss_time = 0
    if total_miss_time == 0 :
        miss_avg_time = 0
        stat_dict['miss_avg_dur'] = str(miss_avg_time) + 's'
    else:
        miss_avg_time = total_miss_time / n_misses  
        stat_dict['miss_avg_dur'] = str(miss_avg_time) + 's'

    #* Average hit time
    #! Here we have to watch out in case total_hit_time = 0

    if total_hit_time == 0:
        hit_avg_time = 0
        stat_dict['hit_avg_dur'] = str(hit_avg_time) + 's'
    else:
        hit_avg_time = total_hit_time / stat_dict['n_hits']
        stat_dict['hit_avg_dur'] = str(hit_avg_time) + 's'

    #* Types
    stat_dict['types'] = inputs
    return stat_dict


#Main

def main():
    
    parser = argparse.ArgumentParser(description='Script for testing typing speed and accuracy') 
    parser.add_argument('--utm',action='store_true',default = False ,help='Use timed mode : tests up to max_value seconds.\n Otherwise tests up to max_value letters')
    parser.add_argument('-mv','--max_value',type=int,required=True,help='Number of seconds/letters of the test') 
    args = parser.parse_args()

    inputs = [] #* This will be the list of namedTuples that the function buildDict will use to build the statistics dictionary
    my_dict = {}

    #//time_b4_exec = time.time() # In order to build the dictionary the buildDict should receive a absolute time as well.
    # The line above would be wrong because it wouldn't take into consideration the time for the user to start nor the countdown

    if args.utm == True:
        inputs ,time_b4_exec = modoTimed(args.max_value)
    else:
        inputs ,time_b4_exec = modoCount(args.max_value)
        
    #At this point in the programm there should already be the list of namedTuples on which the buildDict function will work with
    my_dict = buildDict(inputs,time_b4_exec)
    pprint.pprint(my_dict)


    


if __name__=='__main__':
    main()
