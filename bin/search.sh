#!/usr/bin/env bash

# search.sh - given a TSV file, search our corpora

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 25, 2021 - first cut; while in Lancaster


# configure
NGRAMS='./bin/ngrams.sh'
QUERIES='./etc/queries.tsv'

# process each query
cat $QUERIES | while read N PATTERN CORPUS FILE; do
	
		# debug
		#echo -e "        n: $N"       >&2
		#echo -e "  pattern: $PATTERN" >&2
		#echo -e "   corpus: $CORPUS" >&2
		#echo -e "     file: $FILE"    >&2
		#echo                       >&2
		
		# do the work in the background
		COMMAND="$NGRAMS $N $PATTERN $CORPUS"
		$COMMAND > $FILE &
				
# done
done

# hang out and fini
wait
exit
