# /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# From https://textblob.readthedocs.io/en/dev/quickstart.html
#
from __future__ import print_function
import textblob
from textblob.np_extractors import ConllExtractor
import sys
import optparse
parser = optparse.OptionParser()
parser.add_option("--tags", action="store_true", default=False)
parser.add_option("--tokens", action="store_true", default=False)
parser.add_option("--parsed", action="store_true", default=False)
parser.add_option("--sentiment", action="store_true", default=False)
parser.add_option('-f', '--file', dest="input_filename", default=None )
parser.add_option("-s", "--sentence", dest="sentence", default=None)
options, args = parser.parse_args(sys.argv)

# print("options is", options)
# print("args is ", args )
if options.input_filename is not None :
    in_file = open ( options.input_filename, "r", encoding='utf-8', errors='ignore')
    in_file_text = "\n".join( in_file.readlines() )
elif options.sentence is not None :
    in_file_text = options.sentence
else :
    in_file_text = raw_input("Enter a sentence")



extractor = ConllExtractor()
try:
    blob = textblob.TextBlob(in_file_text, np_extractor=extractor)
except UnicodeDecodeError as e:
    print("Threw a UnicodeDecodeError {} in_file_text is \n".format(str(e)))
    print(in_file_text)
    pdb.set_trace()
    sys.exit(1)

# From https://media.readthedocs.org/pdf/textblob/0.8.2/textblob.pdf
if options.tags :
    print ( "Tags: ", blob.tags)
if options.tokens :
    print ( "Tokens: ", blob.tokenize() )
if options.parsed :
    print ( "Parsed: ", blob.parse() )
if options.sentiment :
    print ( "sentiment: Polarity {:.2f} subjectivity {:.2f} ".format(blob.sentiment.polarity, blob.sentiment.subjectivity ) )

# http://textblob.readthedocs.io/en/dev/quickstart.html


