import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode
from split_nodes import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        node1 = TextNode("This is text with a ", TextType.TEXT)
        node2 = TextNode("code block", TextType.CODE)
        node3 = TextNode(" word", TextType.TEXT)

        self.assertEqual(new_nodes, [node1, node2, node3])
 


if __name__ == "__main__":
    unittest.main()
