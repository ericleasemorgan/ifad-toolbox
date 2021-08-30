# IFAD Toolbox

How are different words and phrases used in a given corpus? Such is the sort of question this suite of tools is designed to address.

More specifically, a set of 200 PDF files complete with rudimentary bibliographic metadata was used as input to a system called the Distant Reader. The result is/was a data set -- a set of structured data intended for computation. The corpus is approximately 1.5 million words long. (By comparison, the novel Moby Dick is .2 million words long.) This distribution augments the data set, queries the result, and outputs simple tables intended to illustrate the results.


## Contents

This distribution includes the following scripts intended to be used in the following order:

   1. ./bin/add-columns.sh - augments the underlying Distant Reader study carrel database with additional columns in the bib table; this script need only be used once, but there no harm done if it is run multiple times

   2. ./bin/update-columns.py - reads ./study-carrel/metadata.csv, and adds content to the newly created columns of the bib table; this script need only be used once, but there no harm done if it is run multiple times

   3. ./bin/create-subcorpora.py - reads the values in the newly created columns, and creates sets of subcorpora in the ./subcorpora directory; this script need only be used once, and it has already been run, but there no harm done if it is run multiple times

   4. ./bin/build.sh - performs all of the previous actions in one script; this script need only be used once, and it has already been run, but there no harm done if it is run multiple times

   5. ./bin/concordance.py - given the name of a file and a word/phrase, output lines containing the word/phrase; this is a keyword-in-context index, or a poor man's search engine

   6. ./bin/ngrams.py - given a file and an integer, output ngrams; this is used to merely list the one-word, two-word, three-word, etc. phrases in the file

   7. ./bin/ngrams.sh - given a file, an integer, and a regular expression, output a tab-delimited file listing a file found in the ./subcorpora directory and the relative number of times the regular expression occurs

   8. ./bin/size.py - used internally, compute the size of the whole corpus, sans stop words; used to compute the relative weight of a search result returned in ./bin/search.sh
   
   9. ./bin/search.sh - given a set of queries (./etc/queries.tsv), run ./bin/ngrams.sh and output a corresponding set of .tsv files listing relative weights of queries
   
  10. ./bin/merge.sh - given the .tsv files found in ./tables, amalgamate all the .tsv files into a single .csv file intended for visualization


## Usage

Using the scripts in this distribution is an iterative process:

   1. Run ./bin/build.sh to ultimately create two different sets of corpora

   2. Use both concordance.py and ngrams.py to identify words or phrases of interest.

   3. With the understanding that an idea be manifested in a number of different forms (plurals, stems, etc.), render the word or phrase as a regular expression. This is by far the most difficult part of the process.

   4. Use ./bin/ngrams.sh to test queries and validate results

   5. Create ./etc/queries.tsv denoting a set of searches. The file requires 4 columns: 1) an integer denoting the size of an ngram, 2) a regular expression; the thing to search, 3) the directory of the corpora to query; either corpora or subcorpora, and 4) the name of the file to send results

   6. Run ./bin/search.sh to loop through the queries and save .tsv files in ./tables
   
   7. Run ./bin/merge.py to create a single .csv file from all the .tsv files in ./tables. The output will be a file named ./table.csv, and you might want to rename this file in order to keep in distinct from others
   
   8. Go to Step #5 and change the value of column 3 from "corpora" to "subcorpora" or vice versa
   
   9. Go to Step #1; this is never-ending work


## Examples

Here are number of examples:

   * ./bin/build.sh
   * ./bin/concordance.py
   * ./bin/concordance.py ./study-carrel/etc/reader.txt farmer
   * ./bin/concordance.py ./study-carrel/etc/reader.txt "small farmer"
   * ./bin/ngrams.py
   * ./bin/ngrams.py ./study-carrel/etc/reader.txt 1
   * ./bin/ngrams.py ./study-carrel/etc/reader.txt 2
   * ./bin/ngrams.py ./study-carrel/etc/reader.txt 2 | sort | uniq -c | sort -rn | less
   * ./bin/ngrams.py ./study-carrel/etc/reader.txt 1 | grep 'smallhold' | sort | uniq -c | sort -rn | less
   * ./bin/ngrams.py ./study-carrel/etc/reader.txt 2 | grep '^small\Wfarm' | sort | uniq -c | sort -rn | less
   * ./bin/ngrams.sh
   * ./bin/ngrams.sh 2 '^small\Wfarm' > ./tables/small-farm.tsv
   * (create/edit ./etc/queries.tsv)
   * ./bin/search.sh
   * ./bin/merge.py
   * mv table.csv ./tables/corpora.csv
   * (edit ./etc/queries.tsv)
   * ./bin/search.sh
   * ./bin/merge.py
   * mv table.csv ./tables/subcorpora.csv
   * (use your spreadsheet program to open the .csv files and visualize the results)


## Summary

This is the beginnings of a suite of tools used to quickly use and understand the content of specifically shaped corpus. I'm sure bugs will be found along the way, and I'm sure there are ways the suite can be improved.

--- 
Eric Lease Morgan  
August 30, 2021

   