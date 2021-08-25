#!/usr/bin/env python

# merge.py - given a directory of TSV files, output a concatenation of ech

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 25, 2021 - first cut; while in Lancaster


# configure
DIRECTORY = './tables'

# require
from pathlib  import Path
import pandas as     pd

# get a list of all files; tricky
files = [ file for file in Path( DIRECTORY ).glob( '*.tsv' ) ]

# initialize
table = pd.read_csv( str( files[ 0 ] ), sep='\t' )

# process every other file
for i in range( 1, len( files ) ) :

	dataframe = pd.read_csv( str( files[ i ] ), sep='\t' )
	table = pd.merge( table, dataframe )

table.to_csv( 'table.csv', index=False )
