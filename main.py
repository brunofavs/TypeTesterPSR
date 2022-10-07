#!/usr/bin/env python3

#Conventions

#! camelCase for functions and methods
#! snake_cae for variables

# Imports
import argparse
import random
from collections import namedtuple
import readchar

import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)

#Global Variables

input_tuple=namedtuple('input_tuple',['l_s','l_t','t'])

#Functions


#Main

def main():
    
    parser = argparse.ArgumentParser(description='Script for testing typing speed and accuracy') 
    parser.add_argument('--utm',action='store_true',default = False ,help='Use timed mode : tests up to max_value seconds.\n Otherwise tests up to max_value letters')
    parser.add_argument('-mv','--max_value',type=int,required=True,help='Number of seconds/letters of the test') 
    args = parser.parse_args()

   




if __name__=='__main__':
    main()
