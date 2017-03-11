#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import spacy
import numpy

print( "Creating an nlp object", file=sys.stderr )
nlp = spacy.load('en')
print ("Thinking....", file=sys.stderr )
apples, and_, oranges = nlp(u'apples and oranges')
print(apples.vector.shape)
# (1,)
print(apples.similarity(oranges) )

print ("Thinking....", file=sys.stderr )
apples, and_, trains = nlp(u'apples and locomotives')
print(apples.vector.shape)
# (1,)
print( apples.similarity(trains) )

