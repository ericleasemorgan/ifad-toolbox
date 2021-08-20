#!/usr/bin/env bash

# ngrams.sh - a front-end to ngrams.py

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 10, 2021 - first cut


# configure
NGRAMS='./bin/ngrams.py'
SIZE='./bin/size.py'
MULTIPLIER=10000
SCALE=7

# sanity check; get input
if [[ -z $1 || -z $2 || -z $3 ]]; then
	echo "Usage: $0 <n> <pattern> [corpora|subcorpora]" >&2
	exit
fi

# get input
N=$1
PATTERN=$2
DIRECTORY=$3

# process each subcorpus
find $DIRECTORY -type f | sort | while read FILE; do

	# create pretty filename (mostly) and debug
	BASENAME=$( basename $FILE '.txt' )
	echo "       basename: $BASENAME" >&2
	
	# count the number of occurrences
	NUMERATOR=$( $NGRAMS $FILE $N | grep -c $PATTERN )
	echo "          count: $NUMERATOR" >&2
	
	# get the size of the (sub)corpus
	DENOMERATOR=$( $SIZE $FILE )
	echo "           size: $DENOMERATOR" >&2

	# calculate the relative number of occurrences
	RELATIVESIZE=$( echo "scale=$SCALE; $NUMERATOR/$DENOMERATOR*$MULTIPLIER" | bc )
	echo "  relative size: $RELATIVESIZE" >&2

	# output
	printf "$BASENAME\t$RELATIVESIZE\n"

    # prettify
    echo >&2
    	
done
exit


