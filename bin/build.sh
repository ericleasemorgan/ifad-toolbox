#!/usr/bin/env bash

# build.sh - one script to initialize the data set

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 13, 2021 - first cut; using brute force, and assume the script work correctly


# add columns to the underlying study carrel database
echo "Adding columns. Errors about duplicate columns are probably okay..." >&2
./bin/add-columns.sh

# update the newly created fields with data
echo "Updating columns..." >&2
./bin/update-columns.py

# create subcorpora
echo "Creating subcorpora..." >&2
./bin/create-subcorpora.py author
./bin/create-subcorpora.py region
./bin/create-subcorpora.py date

# done
echo "Done. You can now use concordance.py, ngrams.py, and ngrams.sh to do analysis." >&2
exit
