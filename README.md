# funny-words
A Python script that generates a list of pairs of funny words for naming things such as app releases, internal projects, servers and children.

Forked this from sethblack. Updated with some new features just to kill some time. Added more silly words and the ability to select what letters the words should start with. 

# Installation

```sh
python setup.py install
```

# Usage
```sh
funny-words [-n] [-w] [-d] [-s] [-a]

-n, --number     how many lines of funny words to generate
-w, --words      how many funny words to generate per line
-d, --delimiter  what to put between the funny words
-s, --start      Force the first word to start with a specific letter
-a, --allstart   Force all word to start with a specific letter
```