import re

from trie import Trie

DICTIONARY = "/usr/share/dict/words"
trie = Trie()

with open(DICTIONARY) as f:
    word = f.readline().lower()
    while word:
        word = f.readline().lower().rstrip()
        if(re.match(r'^[a-z]+$', word)):
            trie.insert(word)
