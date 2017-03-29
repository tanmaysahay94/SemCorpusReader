#!/bin/env python

import os
import itertools
from lxml import html

class CustomSemCorCorpusReader(object):

    def __init__(self, pathToSemCorCorpus, fileName='br-a01'):
        self.pathToSemCorCorpus     = None
        self.fileName               = None
        self.pathToFile             = None
        self._raw                   = None
        self._annotated_chunks      = None
        self._wnsn_tagged_chunks    = None
        self._pos_tagged_chunks     = None
        self._lemma_tagged_chunks   = None
        try:
            assert os.path.exists(pathToSemCorCorpus) is True
            self.pathToSemCorCorpus = pathToSemCorCorpus
            try:
                self.pathToFile         = self.findPathToFile(fileName, pathToSemCorCorpus)
                assert self.pathToFile is not None
                self.fileName           = fileName
            except:
                raise IOError("{} not found in {}...".format(fileName, pathToSemCorCorpus))
        except:
            raise IOError("{} is an invalid filepath...".format(pathToSemCorCorpus))

    def findPathToFile(self, target, directory):
        for root, dirs, files in os.walk(directory):
            for name in files:
                if name == target:
                    return os.path.join(root, name)
        return None

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
