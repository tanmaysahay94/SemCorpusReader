SemCorpusReader
=====
A library that reads SemCor corpus data and provides various data points and attributes related to them programatically.

Install
=====
Download the library on to your system.
Having done that, add the following line to the end of your ```~/.bashrc``` file:
```
export PYTHONPATH=$PYTHONPATH:path/to/parent/of/SemCorpusReader.py
```
For example, if the path to ```SemCorpusReader.py``` is ```~/work/readers/SemCorpusReader/SemCorpusReader.py```, then your command would be
```
export PYTHONPATH=$PYTHONPATH:~/work/readers/SemCorpusReader
```
Run the following command to refresh your environment variables:
```
$ source ~/.bashrc
```

Usage
=====
```
$ python
>>> from SemCorpusReader import SemCorpusReader as scr
>>> reader = scr('../semcor3.0/', 'br-a02')         # '../semcor3.0/' is the relative path to the corpus and 'br-a02' is the name of the file to be read. You may choose to not pass filename
>>> reader.fileids()                                # returns fileids of dataset
['brown1/tagfiles/br-a01',
 'brown1/tagfiles/br-a02',
 .
 .
 .
]
>>> reader.annotated_chunks()                       # returns all sentences in the file in the form of annotated chunks
[[({'lemma': 'committee', 'cmd': 'done', 'wnsn': '1', 'pos': 'NN', 'lexsn': '1:14:00::'},
        ['Committee']),
  ({'lemma': 'approval', 'cmd': 'done', 'wnsn': '1', 'pos': 'NN', 'lexsn': '1:04:02::'},
     ['approval']),
  ({'cmd': 'ignore', 'pos': 'IN'}, ['of']),
  ({'pn': 'person', 'cmd': 'done', 'lexsn': '1:03:00::', 'pos': 'NNP', 'lemma': 'person', 'rdf': 'person', 'wnsn': '1'},
     ['Gov._Price_Daniel']),
  ({'cmd': 'ignore', 'pos': 'POS'}, ["'s"]),
  ({'lemma': 'abandoned', 'cmd': 'done', 'wnsn': '1', 'pos': 'JJ', 'lexsn': '5:00:00:uninhabited:00'},
     ['abandoned']),
  ({'lemma': 'property', 'cmd': 'done', 'wnsn': '1', 'pos': 'NN', 'lexsn': '1:21:00::'},
     ['property']),
  ({'lemma': 'act', 'cmd': 'done', 'wnsn': '1', 'pos': 'NN', 'lexsn': '1:10:01::'},
     ['act']),
  ({'lemma': 'seem', 'cmd': 'done', 'wnsn': '1', 'pos': 'VB', 'lexsn': '2:39:00::'},
     ['seemed']),
  ({'lemma': 'certain', 'cmd': 'done', 'wnsn': '4', 'pos': 'JJ', 'lexsn': '3:00:03::'},
     ['certain']),
  ({'lemma': 'thursday', 'cmd': 'done', 'wnsn': '1', 'pos': 'NN', 'lexsn': '1:28:00::'},
     ['Thursday']),
  ({'cmd': 'ignore', 'pos': 'IN'}, ['despite']),
  ({'cmd': 'ignore', 'pos': 'DT'}, ['the']),
  ({'lemma': 'adamant', 'cmd': 'done', 'wnsn': '1', 'pos': 'JJ', 'lexsn': '5:00:00:inflexible:02'},
     ['adamant']),
  ({'lemma': 'protest', 'cmd': 'done', 'wnsn': '1', 'pos': 'NN', 'lexsn': '1:10:00::'},
     ['protests']),
  ({'cmd': 'ignore', 'pos': 'IN'}, ['of']),
  ({'lemma': 'texas', 'cmd': 'done', 'wnsn': '1', 'pos': 'NN', 'lexsn': '1:15:00::'},
     ['Texas']),
  ({'lemma': 'banker', 'cmd': 'done', 'wnsn': '1', 'pos': 'NN', 'lexsn': '1:18:00::'},
     ['bankers'])],
  .
  .
  .
]
>>> reader.wnsn_tagged_chunks()                     # returns all sentences of file with their chunks tagged with WordNet synset number
[[('1', ['Committee']),
  ('1', ['approval']),
  (None, ['of']),
  ('1', ['Gov._Price_Daniel']),
  (None, ["'s"]),
  ('1', ['abandoned']),
  ('1', ['property']),
  ('1', ['act']),
  ('1', ['seemed']),
  ('4', ['certain']),
  ('1', ['Thursday']),
  (None, ['despite']),
  (None, ['the']),
  ('1', ['adamant']),
  ('1', ['protests']),
  (None, ['of']),
  ('1', ['Texas']),
  ('1', ['bankers'])],
 .
 .
 .
]
```
