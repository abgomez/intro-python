#Abel Gomez 80602216
#01/18/2018
#The program takes and input file then it keeps track of the total number of times each word occurs in it, 
#arguments: input and output files names. 
#Use: wordCount.py <inputFile> <outputFile>

import sys
if len(sys.argv) != 2:
	print 'Incorrect number of arguments'
else: 
	print sys.argv[1]
