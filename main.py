#!/usr/bin/env python3

#Conventions

#! camelCase for functions and methods
#! snake_case for variables

# Imports

import argparse
from asyncio import wait_for
from concurrent.futures import wait
import random
from collections import namedtuple
import sys
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
    
    #for i in range(1,)
    


def modoTimed(threshold):

    print('The test will begin shortly, ending after ' + str(threshold) + ' seconds.')
    print('Press any key to begin the test')
    getch.getch()                                       #! See line 17 
    timed_inputs = []

    # After pressing a key, there's a 3 second countdown before the test starts for the user to prepare.
    for i in range(1,4):
        print('The test will start in '+ str(4-i) +' seconds.')
        time.sleep(1)


    time_b4 = time.time()                               #Stores the time when the test was started
    timing = 0                                          #Define value 0 to the variable that is going to be used during the while cycle

    #The function will run until the duration limit is reached
    while not timing >= float(threshold):

        correct_letter = random.randint(97,122)         #Generates a random letter
        print('Type letter "',chr(correct_letter),'"')  #Prints the generated letter
        time_b4_chr = time.time()                       #Gets the time before the input

        typed_letter = readchar.readkey()               #Reads the input letter
        time_after = time.time()                        #Gets the time after the input 
        reaction_time = time_after - time_b4_chr        #Reaction time
        timing = time_after - time_b4                   #Elapsed time
        
        if  typed_letter == chr(32):                    #Clicking on the space bar 
            time_after = time.time()                    #End date of the text
            break
        
        #TODO se esperarmos algum tempo e só depois carregarmos no espaço, a data de fim não vai corresponder ao tempo de reação
        print("You typed",typed_letter, '\n')           #Prints the typed letter
        input=(correct_letter, ord(typed_letter), reaction_time ) #Stores the information from the test
        timed_inputs.append(input)
    
    print('Test is finished!!')
    print(timed_inputs)
    print(time_b4)
    return(timed_inputs, time_b4)

    # TODO Yet to implement
    # return timed_inputs

def buildDict(inputs):
    pass

    # return {accuracy:blablalba}


#Main

def main():
    
    parser = argparse.ArgumentParser(description='Script for testing typing speed and accuracy') 
    parser.add_argument('-utm','--use_time_mode', action='store_true',default = False ,help='Use timed mode : tests up to max_value seconds.\n Otherwise tests up to max_value letters')
    parser.add_argument('-mv','--max_value',type=int,required=True,help='Number of seconds/letters of the test') 
    args = parser.parse_args()

    inputs = [] #* This will be the list of namedTuples that the function buildDict will use to build the statistics dictionary
    my_dict = {}

    if args.use_time_mode == True:
        inputs = modoTimed(args.max_value)
    else:
        inputs = modoCount(args.max_value)
        
    #At this point in the program there should already be the list of namedTuples on which the buildDict function will work with
    my_dict = buildDict(inputs)
    print(my_dict) #! --> prints 'none' because buildDict returns void


    


if __name__=='__main__':
    main()
