"""
Basic prefix tree with only insert, search and search for prefix operations.

TODO:
    -return all words with certain prefix
"""

import unittest

class TrieNode():
    def __init__(self):
        self.leaf = False
        self.edges = [None] * 26

class Trie():
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        return self._insert(self.root, word)


    def _insert(self, vertex, word):
        if not word:
            vertex.leaf = True
        else:
            c = ord(word[0]) - ord('a')
            if not vertex.edges[c]:
                vertex.edges[c] = TrieNode()
            self._insert(vertex.edges[c], word[1:])


    def search(self, word):
        return self._search(self.root, word)


    def _search(self, vertex, word):
        if not word:
            return vertex.leaf
        c = ord(word[0]) - ord('a')
        if not vertex.edges[c]:
            return False
        else:
            return self._search(vertex.edges[c], word[1:])


    def search_prefix(self, prefix):
        return self._search_prefix(self.root, prefix)


    def _search_prefix(self, vertex, prefix):
        if not prefix:
            return True
        c = ord(prefix[0]) - ord('a')
        if not vertex.edges[c]:
            return False
        else:
            return self._search_prefix(vertex.edges[c], prefix[1:])


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.t = Trie()
        self.t.insert("foo")
        self.t.insert("foobar")
        self.t.insert("bar")
        self.t.insert("baz")

    def test_search(self):
        self.assertEqual(True, self.t.search("foo"))
        self.assertEqual(True, self.t.search("foobar"))
        self.assertEqual(True, self.t.search("bar"))
        self.assertEqual(True, self.t.search("baz"))
        self.assertEqual(False, self.t.search("foob"))
        self.assertEqual(False, self.t.search("barr"))
        self.assertEqual(False, self.t.search("quux"))

    def test_search_prefix(self):
        self.assertEqual(True, self.t.search_prefix("f"))
        self.assertEqual(True, self.t.search_prefix("fo"))
        self.assertEqual(True, self.t.search_prefix("foo"))
        self.assertEqual(True, self.t.search_prefix("foobar"))
        self.assertEqual(True, self.t.search_prefix("b"))
        self.assertEqual(True, self.t.search_prefix("ba"))
        self.assertEqual(False, self.t.search_prefix("fa"))
        self.assertEqual(False, self.t.search_prefix("bb"))

if __name__ == '__main__':
    unittest.main()
