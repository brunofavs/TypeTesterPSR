#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(description='Computes the perfect numbers up to x') 
parser.add_argument('--max_number',action='store_true',default = False ,help='x') 
args = parser.parse_args()

print(args.max_number)