#! /usr/bin/python
#
# This is from http://www.nltk.org/book/ch07.html

from __future__ import print_function
import nltk
import termcolor
import sys
import codecs     # Python 2.7 and earlier only



cp = nltk.RegexpParser(grammar)

def tokenize_document ( document_lst ):
  """This is from http://www.nltk.org/book/ch07.html"""

# Document should be a list of strings.  Each string should be a sentence.
  if type(document_lst) == type([]) :
    document = " ".join(document_lst)
  else :
    document = document_lst
  sentences = nltk.sent_tokenize(document)
  words = [nltk.word_tokenize(sent) for sent in sentences]
  tagged_sentences = [nltk.pos_tag(word) for word in words]
  result = list()
  for tagged_sentence in tagged_sentences :
    result.append ( cp.parse(tagged_sentence) )
  return result






if __name__ == "__main__" :

  if sys.argv[1] == "-f" :
    print ( "Reading the file", file=sys.stderr )
    with codecs.open(sys.argv[2], "r",  encoding='utf-8', errors='replace' ) as fp :
      document = fp.readlines()
  else :
# Document is on the comamand line
    document = sys.argv[1]

  print ( "Striping the file", file=sys.stderr )
  for i in range( len( document ) ) :
    document[i].strip()

#  print ( document )

  print ( "Tokenizing the file", file=sys.stderr )
  results = tokenize_document ( document )

  for r in results :
    print ( r )






