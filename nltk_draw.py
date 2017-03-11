#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
from nltk.corpus import treebank
t = treebank.parsed_sents('/home/jeffs/nltk_data/corpora/treebank/combined/wsj_0001.mrg')[0]
t.draw()

