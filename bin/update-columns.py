#!/usr/bin/env python

# update-columns.py - given a specifically shaped CSV file, update a database

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 9, 2021 - first investigations


# configure
METADATA = './study-carrel/metadata.csv'
DB       = './study-carrel/etc/reader.db'
UPDATE   = "UPDATE bib SET country='%s', region='%s', amount=%s WHERE id='%s';"

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
	amount  = row[ 'amount' ]
	file    = row[ 'file' ]
	
	# normalize, escape quotes, create key, and create sql
	amount  = str( amount )
	country = country.replace( "'", "''" )
	region  = region.replace( "'", "''" )
	key     = file.replace( '.pdf', '' )
	sql     = ( UPDATE % ( country, region, amount, key ) )
		
	# debug
	stderr.write( '\t'.join( [ key, country, region, amount ] ) + '\n' )
	stderr.write( sql + '\n' )
	
	# do the work
	connection.execute( sql )
	connection.commit()

# done; straight-forward
exit

	