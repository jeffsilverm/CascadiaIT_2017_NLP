# /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# From https://textblob.readthedocs.io/en/dev/quickstart.html
#
import textblob
from textblob.np_extractors import ConllExtractor

if sys.argv[1] == "-f"  :
    in_file_name = sys.argv[2]
    in_file = open(in_file_name, "r")
    in_file_text = read_file_and_scrub.read_file_and_scrub(in_file)
else :
    in_file_text = sys.argv[2]



extractor = ConllExtractor()
try:
    blob = TextBlob(in_file_text, np_extractor=extractor)
except UnicodeDecodeError as e:
    print("Threw a UnicodeDecodeError {} in_file_text is \n".format(str(e)))
    print(in_file_text)
    pdb.set_trace()
    sys.exit(1)

# From https://media.readthedocs.org/pdf/textblob/0.8.2/textblob.pdf
print ( blob.noun_phrases )
