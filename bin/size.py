#!/usr/bin/env python

# size.py - given a file, output its size in words


# configure
STOPWORDS = './study-carrel/etc/stopwords.txt'

# require
import sys
import nltk

# get input
if len( sys.argv ) != 2 : sys.exit( "Usage: " + sys.argv[ 0 ] + " <file>" )
file = sys.argv[ 1 ]

# initialize
stopwords = open( STOPWORDS ).read().split()

# read, tokenize, and normalize the text
text   = open( file ).read()
tokens = nltk.word_tokenize( text, preserve_line=True )
tokens = [ token.lower() for token in tokens if token.isalpha() ]

# do the work and done
print( len( tokens ) )
exit()