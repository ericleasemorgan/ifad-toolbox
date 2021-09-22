#!/usr/bin/env python

# update-columns.py - given a specifically shaped CSV file, update a database

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 9, 2021 - first investigations


# configure
METADATA = './study-carrel/metadata.csv'
DB       = './study-carrel/etc/reader.db'
UPDATE   = "UPDATE bib SET country='%s', region='%s', amount=%s WHERE id='%s';"
UPPER    = 'UPDATE bib SET author = UPPER( author );'

# require
from   sys     import stderr
import pandas  as pd
import sqlite3 

# initialize and connect to the database
metadata   = pd.read_csv( METADATA )
connection = sqlite3.connect( DB )

# loop through each row
for index, row in metadata.iterrows() :
	
	# parse
	country = row[ 'country' ]
	region  = row[ 'region' ]
	finance = row[ 'finance' ]
	file    = row[ 'file' ]
	
	# normalize, escape quotes, create key, and create sql
	finance = str( finance )
	country = country.replace( "'", "''" )
	region  = region.replace( "'", "''" )
	key     = file.replace( '.txt', '' )
	sql     = ( UPDATE % ( country, region, finance, key ) )
		
	# debug
	stderr.write( '\t'.join( [ key, country, region, finance ] ) + '\n' )
	stderr.write( sql + '\n' )
	
	# do the work
	connection.execute( sql )
	connection.commit()
	
# normalize case of authors
connection.execute( UPPER )
connection.commit()

# done
exit

	