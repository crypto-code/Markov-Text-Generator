import nltk
import re
import pprint
import random
import sys
import getopt 
import glob
import MarkovChain as markov



def main(maxWordInSentence, dictFile, genNSentences=50):

	#Creates new Markov class
	markovObj = markov.Markov(dictFile=dictFile, maxWordInSentence= maxWordInSentence)

	TotalText = []

	for _ in range( genNSentences ):
		text = markovObj.genText() 
		print(text)
		if len(text) <= 140 and text.endswith('.'):
			TotalText.append(text)

	print("\n\n")

def checkargs():
	keyLen = 1
	maxWordInSentence = 20
	genNSentences = 5
	fileList = []

	if len(sys.argv) < 3:
		print( "Usage: " + sys.argv[0] + " -w <sentence word length> -n <sentences to generate> -d <dictionary file> ")
		exit(0)
	else:
		arg = {}
		options = getopt.getopt(sys.argv[1:], 'k:w:n:d:')
		for item in options[0]:
			if(item):
				arg[ item[0] ] = item[1]

		maxWordInSentence = int(arg[ '-w'])
		genNSentences = int(arg[ '-n' ])
		dictFile = arg['-d']

	return(maxWordInSentence, genNSentences, dictFile)


if __name__ == "__main__":
	(maxWordInSentence, genNSentences, dictFile) = checkargs()

	main(maxWordInSentence, dictFile, genNSentences)
