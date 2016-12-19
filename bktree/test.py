import unittest

import bktree


class BkTreeTest(unittest.TestCase):

    def test_gets_close_words(self):
        words = [0xfe]
        tree = bktree.Tree(words)

        self.assertEqual([node.num for node in tree.search(0xff, 1)], [0xfe])

    def test_finds_far_words(self):
        words = [0x01]
        tree = bktree.Tree(words)

        self.assertEqual([node.num for node in tree.search(0xff, 15)], [0x01])

    def test_empty_search(self):
        words = [0xfe, 0xfd, 0xfb, 0xf7, 0xef, 0xdf, 0xbf, 0x7f]
        tree = bktree.Tree(words)

        self.assertEqual(tree.search(0xff, 0), [])

    def test_search(self):
        a = 0b101
        b = 0b000
        tree = bktree.Tree([a, b])

        self.assertEqual(len(tree.search(b, 2)), 2)
        self.assertEqual(len(tree.search(b, 1)), 1)

if __name__ == '__main__':
    unittest.main()
