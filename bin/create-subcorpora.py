#!/usr/bin/env python

# create-subcorpus.py - given a column name, create subcopora

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 9, 2021 - first investigations


# configure
DB         = './study-carrel/etc/reader.db'
QUERY      = 'SELECT DISTINCT( %s ) FROM bib ORDER BY %s;'
SUBQUERY   = "SELECT id FROM bib WHERE %s='%s';"
EXTENSION  = '.txt'
ROOT       = './study-carrel/txt'
SUBCORPORA = './subcorpora'
PREFIX     = 'region'

# require
import sqlite3 
import sys

# get input
if len( sys.argv ) != 2 : sys.exit( "Usage: " + sys.argv[ 0 ] + " [author|region|date]" )
column = sys.argv[ 1 ]

# initialize
connection             = sqlite3.connect( DB )
connection.row_factory = sqlite3.Row

# find and process each region
query   = ( QUERY % ( column, column ) )
results = connection.execute( query ).fetchall()
for result in results :

	# re-initialize
	field = result[ column ]
	sys.stderr.write( field + '\n' )
	
	# find and process each item; create a corpus
	corpus     = ''
	subquery   = ( SUBQUERY % ( column, field ) )
	subresults = connection.execute( subquery ).fetchall()
	for subresult in subresults :
		
		# get the key and create a file name
		id   = subresult[ 'id' ]
		file = ROOT + '/' + id + EXTENSION
		
		# debug
		sys.stderr.write( file + '\n' )
		
		# read the file and update the corpus
		text    = open( file ).read()
		corpus += text
	
	# create output file name and output
	field = field.replace( ' ', '-' )
	file   = SUBCORPORA + '/' + column + '-' + field + EXTENSION
	with open( file, 'w' ) as handle : handle.write( corpus )

# done
exit

	