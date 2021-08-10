#!/usr/bin/env bash

# add-columns.sh - update the bib table to include additional fields

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 9, 2021 - first cut


# configure
ADDCOLUMNS='./etc/add-columns.sql'
DB='./study-carrel/etc/reader.db'

# do the work and done
cat $ADDCOLUMNS | sqlite3 $DB
exit
