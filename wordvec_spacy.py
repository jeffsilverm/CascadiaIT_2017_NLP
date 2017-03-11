#! /usr/bin/env python
# -*- coding: utf-8 -*-


import spacy
import numpy

nlp = spacy.load('en')
apples, and_, oranges = nlp(u'apples and oranges')
print(apples.vector.shape)
# (1,)
apples.similarity(oranges)

