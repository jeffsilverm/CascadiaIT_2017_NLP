# /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# From https://textblob.readthedocs.io/en/dev/quickstart.html
#
import textblob
from textblob.np_extractors import ConllExtractor
import sys
import optparse
parser = optparse.OptionParser()
parser.add_option("--tags", action="store_true", default=False)
parser.add_option("--tokens", action="store_true", default=False)
parser.add_option("--parsed", action="store_true", default=False)
parser.add_option("--sentiment", action="store_true", default=False)
parser.add_option('-f', '--file', dest="input_filename" )
options, args = parse_args(sys.arv)


if sys.argv[1] == "-f"  :
    in_file_name = sys.argv[2]
    in_file = open(in_file_name, "r", encoding='utf-8', errors='ignore')
    in_file_text = "\n".join( in_file.readlines() )
else :
    in_file_text = sys.argv[1]



extractor = ConllExtractor()
try:
    blob = textblob.TextBlob(in_file_text, np_extractor=extractor)
except UnicodeDecodeError as e:
    print("Threw a UnicodeDecodeError {} in_file_text is \n".format(str(e)))
    print(in_file_text)
    pdb.set_trace()
    sys.exit(1)

# From https://media.readthedocs.org/pdf/textblob/0.8.2/textblob.pdf
print ( "Tags: ", blob.tags)
print ( "Tokens: ", blob.tokenize() )
print ( "Parsed: ", blob.parse() )
print ( "sentiment: Polarity {:.2f} subjectivity {:.2f} ".format(blob.sentiment.polarity, blob.sentiment.subjectivity ) )

# http://textblob.readthedocs.io/en/dev/quickstart.html


