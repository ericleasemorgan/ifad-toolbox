#!/usr/bin/env python

# create-subcorpus.py - given a column name, create subcopora

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 9, 2021 - first investigations


# configure
DB          = './study-carrel/etc/reader.db'
AUTHORS      = 'SELECT DISTINCT( author ) FROM bib ORDER BY author;'
REGIONS      = 'SELECT DISTINCT( region ) FROM bib ORDER BY region;'
DATES        = 'SELECT DISTINCT( date )   FROM bib ORDER BY date;'
AUTHORDATE   = "SELECT id FROM bib WHERE author='%s' AND date='%s';"
DATEREGION   = "SELECT id FROM bib WHERE date='%s'   AND region='%s';"
REGIONAUTHOR = "SELECT id FROM bib WHERE region='%s' AND author='%s';"
EXTENSION    = '.txt'
ROOT         = './study-carrel/txt'
SUBCORPORA   = './subcorpora'

# require
import sqlite3 
import sys

# initialize
connection             = sqlite3.connect( DB )
connection.row_factory = sqlite3.Row

# given a list of ids, output a plain text file
def ids2files( ids, category, field, subfield ) :

	# initialize
	corpus = ''

	# process each id
	for id in ids :
		
		# get the key and create a file name
		id   = id[ 'id' ]
		file = ROOT + '/' + id + EXTENSION
				
		# read the file and update the corpus
		text    = open( file ).read()
		corpus += text

	# create an output file name and... output
	field    = field.replace( ' ', '-' )
	subfield = subfield.replace( ' ', '-' )
	file     = SUBCORPORA + '/' + category + '_' + field + '-' + subfield + EXTENSION
	with open( file, 'w' ) as handle : handle.write( corpus )
	

# get authors (institutions), dates, and regions
authors = connection.execute( AUTHORS ).fetchall()
dates   = connection.execute( DATES ).fetchall()
regions = connection.execute( REGIONS ).fetchall()

# create author files
for author in authors :

	# re-initialize
	author = author[ 'author' ]
	
	# process each date
	for date in dates :
	
		# re-initialize
		date = date[ 'date' ]
		
		# create a query
		query = ( AUTHORDATE % ( author, date ) )
		ids = connection.execute( query ).fetchall()
		
		# process each result
		ids2files( ids, 'author', author, date )
		

# create date files
for date in dates :

	# re-initialize
	date = date[ 'date' ]
	
	# process each region
	for region in regions :
	
		# re-initialize
		region = region[ 'region' ]
		
		# create a query
		query = ( DATEREGION % ( date, region ) )
		ids = connection.execute( query ).fetchall()
		
		# process each result
		ids2files( ids, 'date', date, region )

# create region files
for region in regions :

	# re-initialize
	region = region[ 'region' ]
	
	# process each author (institution)
	for author in authors :
	
		# re-initialize
		author = author[ 'author' ]
		
		# create a query
		query = ( REGIONAUTHOR % ( region, author ) )
		ids = connection.execute( query ).fetchall()
		
		# process each result
		ids2files( ids, 'region', region, author )

# done
exit

	