#!/usr/bin/env python

# ngrams.py - given a file and an integer, output ngrams


# configure
STOPWORDS = './study-carrel/etc/stopwords.txt'

# require
from   re  import search
import sys
import nltk

# get input
if len( sys.argv ) != 3 : sys.exit( "Usage: " + sys.argv[ 0 ] + " <file> <n>" )
file = sys.argv[ 1 ]
n    = int( sys.argv[ 2 ] )

# initialize
stopwords = open( STOPWORDS ).read().split()

# read, tokenize, and normalize the text
text   = open( file ).read()
tokens = nltk.word_tokenize( text, preserve_line=True )
tokens = [ token.lower() for token in tokens if token.isalpha() ]

# create the set of ngrams; the magic happens here
ngrams = list( nltk.ngrams( tokens, n ) )

# remove stopwords from unigrams or bigrams
if n < 3 :

	# initialize
	results = []
	
	# process each ngram
	for ngram in ngrams :

		# re-initialize
		found = False
		
		# process each token in the ngram
		for token in ngram :

			# check for stopword
			if token in stopwords : found = True

		# conditionally update the results
		if not found : results.append( ngram )

	# done; make it read pretty
	ngrams = results

# output and done
for ngram in ngrams : print( "\t".join( list( ngram ) ) )