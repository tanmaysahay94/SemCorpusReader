#!/usr/bin/env python

"""customSemCorCorpusReader.py: Contains the class CustomSemCorCorpusReader which enables reading and using SemCor corpus"""

import os
import itertools
from lxml import html

class CustomSemCorCorpusReader(object):

    def __init__(self, pathToSemCorCorpus, fileName='br-a02'):
        self._pathToSemCorCorpus    = None
        self._fileName              = None
        self._pathToFile            = None
        self._raw                   = None
        self._annotated_chunks      = None
        self._wnsn_tagged_chunks    = None
        self._pos_tagged_chunks     = None
        self._lemma_tagged_chunks   = None
        self._sents                 = None
        self._fileids               = None
        try:
            assert os.path.exists(pathToSemCorCorpus) is True
            self._pathToSemCorCorpus = pathToSemCorCorpus
            try:
                def _findPathToFile(target, directory):
                    for root, dirs, files in os.walk(directory):
                        for name in files:
                            if name == target:
                                return os.path.join(root, name)
                    return None
                self._pathToFile = _findPathToFile(fileName, pathToSemCorCorpus)
                assert self.pathToFile is not None
                self._fileName = fileName
            except:
                raise IOError("{} not found in {}...".format(fileName, pathToSemCorCorpus))
        except:
            raise IOError("{} is an invalid filepath...".format(pathToSemCorCorpus))

    def pathToSemCorCorpus(self):
        return self._pathToSemCorCorpus

    def fileName(self):
        return self._fileName

    def pathToFile(self):
        return self._pathToFile

    def fileids(self):
        if self._fileids is None:
            self._fileids = [os.path.relpath(path, self.pathToSemCorCorpus()) \
                                for path in \
                                reduce(lambda l1, l2: l1 + l2, [[os.path.join(tup[0], fileid) \
                                for fileid in tup[1]] \
                                for tup in [(root, files) \
                                for root, dirs, files in os.walk(self.pathToSemCorCorpus()) \
                                if root.endswith('tagfiles')]])]
        return self._fileids

    def raw(self):
        if self._raw is None:
            self._raw = open(self.pathToFile).read()
        return self._raw

    def annotated_chunks(self):
        if self._annotated_chunks is None:
            parsed = html.fromstring(self.raw())
            self._annotated_chunks = [(x.tag, x.attrib, x.text.strip().split()) \
                                        for x in parsed.getiterator() \
                                        if x.tag in ['wf', 's']]
            def helper(chunks, splitter='s'):
                return [list(g) for k, g in itertools.groupby(chunks, lambda x: x[0] == splitter) if not k]
            self._annotated_chunks = helper(self._annotated_chunks)
            self._annotated_chunks = [[(attrib, text) for tag, attrib, text in annotated_sentence] \
                                        for annotated_sentence in self._annotated_chunks]
        return self._annotated_chunks

    def _attribute_chunks(self, attribute='pos'):
        return [[(attributes[attribute], chunk) \
                if attribute in attributes else (None, chunk) \
                for attributes, chunk in annotated_sentence] \
                for annotated_sentence in self.annotated_chunks()]

    def wnsn_tagged_chunks(self):
        if self._wnsn_tagged_chunks is None:
            self._wnsn_tagged_chunks = self._attribute_chunks('wnsn')
        return self._wnsn_tagged_chunks

    def pos_tagged_chunks(self):
        if self._pos_tagged_chunks is None:
            self._pos_tagged_chunks = self._attribute_chunks()
        return self._pos_tagged_chunks

    def lemma_tagged_chunks(self):
        if self._lemma_tagged_chunks is None:
            self._lemma_tagged_chunks = self._attribute_chunks('lemma')
        return self._lemma_tagged_chunks

    def sents(self):
        if self._sents is None:
            self._sents = [' '.join(tup[1][0] for tup in annotated_sentence) \
                            for annotated_sentence in self.annotated_chunks()]
        return self._sents


__author__  = "Tanmay Sahay"
__license__ = "MIT"   
