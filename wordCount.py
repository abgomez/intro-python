#abel Gomez 80602216
#01/19/2018
#The program takes and input file then it keeps track of the total number of times each word occurs in it, 
#arguments: input and output files names. 
#Use: wordCount.py <inputFile> <outputFile>

import sys
import re

#check number of arguments if less than 3 exit program
if len(sys.argv) != 2:
	print 'Incorrect number of arguments'
	print 'Correct use wordCount.py <inputFile> <outputFile>'
	quit()

#declare variables
inFileName = sys.argv[1]
regex = '\w+'
unWordList = {}
soWordList = {}

#open input file and count words.
print ('Openning File: %s' % inFileName)
inFile = open(inFileName, 'r')
text = inFile.read()
#use regex to get all words
unWordList = re.findall(r'\w+', text, flags=re.I) 
for word in unWordList:
	word = word.lower()
	#check if the word exists in the output dic, if exists increment count 1 if not add it
	if word in soWordList.keys():
		soWordList[word] += 1
	else:
		soWordList[word] = 1
	
#sort dic. and write to output file.
for word in sorted(soWordList):
	print '%s %s' % (word, soWordList[word]) 


