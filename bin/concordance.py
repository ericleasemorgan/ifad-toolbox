#!/usr/bin/env python

# concordance - given a carrel and a word, output rudimentary keyword-in-context

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 10, 2021 - pulled in from Reader Toolbox


# configure
WIDTH = 80
LINES = 999

# require
from nltk import Text, word_tokenize
import sys

# get input
if len( sys.argv ) != 3 : sys.exit( "Usage: " + sys.argv[ 0 ] + " <file> <query>" )
file  = sys.argv[ 1 ]
query = sys.argv[ 2 ]

# initialize
text = Text( word_tokenize( open( file ).read( ) ) )

# split query into a list, conditionally
if ' ' in query : query = query.split( ' ' )
	
# do the work and output
lines = text.concordance_list( query, width=WIDTH, lines=LINES )
for line in lines : print( line.line )
	