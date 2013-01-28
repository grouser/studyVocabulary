#!/usr/bin/env python

import argparse
import sys
import random

parser = argparse.ArgumentParser()
parser.add_argument('-language', metavar='LANGUAGE', nargs=1, action='store', dest='language', choices=['english', 'spanish'],
                    help='type spanish to read in english and write in spanish, or type english in otherwise.', default=["english"])
parser.add_argument('-text', metavar='FILE', nargs=1, action='store', dest='filename', default=['file.txt'], help='name of the file to read the words')
args = parser.parse_args() 

vocabulary = []

def getWords(filename):
    """
    read the file and create the vocabulary
    """
    
    try:
        f = open(filename, 'r')
    except IOError:
        print "The file %s doesn't exist" % filename
        sys.exit(0)
        
    while True:
        line = f.readline()
        if not line:
            break
        #remove chracter '\n' at the end
        line = line.rstrip()
        w = line.split('=')
        if len(w) == 2:
            vocabulary.append((w[0], w[1]))

def getWord():
    """
    return a word and its traduction
    """
    
    n = random.randint(0, len(vocabulary) - 1)
    word = vocabulary[n]
    
    return word[0], word[1]
    
if __name__ == '__main__':
   getWords(args.filename[0])
   
   while True:
       if args.language[0] == 'english':
           word, traduction = getWord()
       else:
           traduction, word = getWord()
           
       traductions = traduction.split(',')
       #remove whitespace at the beginning or at the end
       traductions = [w.strip() for w in traductions]
       
       answer = raw_input(word + ' = ')
       while (not answer in traductions) and answer != '':
           answer = raw_input(word + ' = ')
           if answer == '':
               break
           