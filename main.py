#!/usr/bin/env python3

#Conventions

#! camelCase for functions and methods
#! snake_case for variables

# Imports

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
    
    #for i in range(1,)
    


def modoTimed(threshold):
    print('The test will begin shortly, ending after ' + str(threshold) + ' seconds.')
    print('Press any key to begin the test')
    getch.getch() # See line 13 

    # After pressing a key, theres a 3 second countdown before the test starts for the user to prepare.
    for i in range(1,4):
        print('The test will start in '+ str(4-i) +' seconds.')
        time.sleep(1)

    # TODO Yet to implement
    # return timed_inputs

def buildDict(inputs):
    pass

    # return {accuracy:blablalba}


#Main

def main():
    
    parser = argparse.ArgumentParser(description='Script for testing typing speed and accuracy') 
    parser.add_argument('--utm',action='store_true',default = False ,help='Use timed mode : tests up to max_value seconds.\n Otherwise tests up to max_value letters')
    parser.add_argument('-mv','--max_value',type=int,required=True,help='Number of seconds/letters of the test') 
    args = parser.parse_args()

    inputs = [] #* This will be the list of namedTuples that the function buildDict will use to build the statistics dictionary
    my_dict = {}

    if args.utm == True:
        inputs = modoTimed(args.max_value)
    else:
        inputs = modoCount(args.max_value)
        
    #At this point in the programm there should already be the list of namedTuples on which the buildDict function will work with
    my_dict = buildDict(inputs)
    print(my_dict) #! --> prints 'none' because buildDict returns void


    


if __name__=='__main__':
    main()
