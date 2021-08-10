#!/usr/bin/env bash

# ngrams.sh - a front-end to ngrams.py

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 10, 2021 - first cut


# configure
SUBCORPORA='./subcorpora'
NGRAMS='./bin/ngrams.py'
HEADER='file\tcount'

# sanity check; get input
if [[ -z $1 || -z $2 ]]; then
	echo "Usage: $0 <n> <pattern>" >&2
	exit
fi

# get input
N=$1
PATTERN=$2

# initialize output
echo -e "$HEADER"

# process each subcorpus
find $SUBCORPORA -type f | sort | while read FILE; do

	# create pretty filename (mostly) and debug
	BASENAME=$( basename $FILE '.txt' )
	echo $BASENAME... >&2
	
	# do the work
	printf "$BASENAME\t"
	$NGRAMS $FILE $N | grep -c $PATTERN

done
exit


