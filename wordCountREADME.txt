The program wordCount.py takes an input file and identifies the number of times each time occurs within the file
it uses regular expressions to search and identify all words. The search and count are case-insensitive. 

The program uses two dictionaries which stores the key and value of each world, one dictionary serves as a middle man
between the input file and the end result. The second dictionary is used to save only unique words and to sort results. 

The program generates an output file where each word with it number of ocurrences are saved. If the output file does not 
exists it will be created.

To run wordCount.py you need to run the following command: python wordCount.py <inputFile> <outputFile>

The functionality of wordCount.py was tested with the script wordCountTest.py, all tests were succesful.

To re run the tests you need to run the following:
test case 1: wordCountTest.py declaration.txt declarationOut.txt declarationKey.txt
test case 2: wordCountTest.py speech.txt speechOut.txt speechKey.txt
