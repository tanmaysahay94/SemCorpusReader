SemCorpusReader
=====

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
```
