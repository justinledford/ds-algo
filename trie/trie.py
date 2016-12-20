"""
Basic prefix tree with only insert, search and search for prefix operations.

TODO:
    -return all words with certain prefix
"""

import unittest

class TrieNode():
    def __init__(self, letter):
        self.word = ""
        self.letter = letter
        self.edges = [None] * 26

class Trie():
    def __init__(self):
        self.root = TrieNode("")


    def insert(self, word):
        return self._insert(self.root, word, word)


    def _insert(self, vertex, prefix, word):
        if not prefix:
            vertex.word = word
        else:
            c = ord(prefix[0]) - ord('a')
            if not vertex.edges[c]:
                vertex.edges[c] = TrieNode(chr(ord('a')+c))
            self._insert(vertex.edges[c], prefix[1:], word)


    def search(self, word):
        return self._search(self.root, word, word)


    def _search(self, vertex, prefix, word):
        if not prefix:
            return vertex.word == word
        c = ord(prefix[0]) - ord('a')
        if not vertex.edges[c]:
            return False
        else:
            return self._search(vertex.edges[c], prefix[1:], word)


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


    def _collect_words(self, vertex):
        words = []
        visited = []
        stack = []

        stack.append(vertex)
        while stack:
            v = stack.pop()
            if v not in visited:
                visited.append(v)
                if v.word != "":
                    words.append(v.word)
                for i, e in enumerate(v.edges):
                    if e is not None:
                        stack.append(e)

        return words


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

    def test_collect_words(self):
        b_vertex = self.t.root.edges[ord('b') - ord('a')]
        f_vertex = self.t.root.edges[ord('f') - ord('a')]
        self.assertEqual(["bar", "baz"].sort(),
                         self.t._collect_words(b_vertex).sort())
        self.assertEqual(["foobar", "foo"].sort(),
                         self.t._collect_words(f_vertex).sort())


if __name__ == '__main__':
    unittest.main()
