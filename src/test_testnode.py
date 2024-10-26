import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is not a test", "bold", url="https://www.hackthissite.org")
        node2 = TextNode("This is not a test", "bold", url="https://www.hackthissite.org")
        self.assertEqual(node1, node2)

    def test_defaulturl(self):
        node = TextNode("This is not a test", "bold")
        self.assertEqual(node.url, None)

    def test_noteq(self):
        node1 = TextNode("This is not a test", "bold", url="https://www.hackthissite.org")
        node2 = TextNode("This is a test", "italic", url="https://www.hackthissite.com")
        self.assertNotEqual(node1, node2)



if __name__ == "__main__":
    unittest.main()
