import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode(tag="p", value="Hello, world")
        node2 = HTMLNode(tag="p", value="Hello, world")
        self.assertEqual(node1, node2)

    def test_props(self):

        node1 = HTMLNode(tag="a", value="this link", 
                         props={"href":"https://www.google.com",
                                "target":"_blank"})
        self.assertEqual(node1.props_to_html(), 
                         ' href="https://www.google.com" target="_blank"')
    def test_defaults(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.props, None)
        self.assertEqual(node.children, None)





class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode(tag="p", value="Hello, world")
        node2 = LeafNode(tag="p", value="Hello, world")
        self.assertEqual(node1, node2)

    def test_props(self):

        node1 = LeafNode(tag="a", value="this link", 
                         props={"href":"https://www.google.com",
                                "target":"_blank"})
        self.assertEqual(node1.props_to_html(), 
                         ' href="https://www.google.com" target="_blank"')
    def test_defaults(self):
        node = LeafNode(value="Hi")
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, "Hi")
        self.assertEqual(node.props, None)
        self.assertEqual(node.children, None)


    def test_tohtml(self):
        node1 = LeafNode(tag="a", value="this link", 
                         props={"href":"https://www.google.com",
                                "target":"_blank"})
        self.assertEqual(node1.to_html(), 
                         '<a href="https://www.google.com" target="_blank">this link</a>')


#node = ParentNode(
#    "p",
#    [
#        LeafNode("b", "Bold text"),
#        LeafNode(None, "Normal text"),
#        LeafNode("i", "italic text"),
#        LeafNode(None, "Normal text"),
#    ],
#)
#
#node.to_html()



class TestParentNode(unittest.TestCase):
    def test_eq(self):
        leaf1 = LeafNode(tag="p", value="Hello, world")
        leaf2 = LeafNode(tag="p", value="Goodbye, world")
        node1 = ParentNode(tag="p", children=[leaf1, leaf2])
        node2 = ParentNode(tag="p", children=[leaf1, leaf2])
        self.assertEqual(node1, node2)


    def test_tohtml(self):
        leaf1 = LeafNode(tag="p", value="Hello, world")
        leaf2 = LeafNode(tag="p", value="Goodbye, world")
        node1 = ParentNode(tag="p", children=[leaf1, leaf2])
        self.assertEqual(node1.to_html(), 
                         "<p><p>Hello, world</p><p>Goodbye, world</p></p>")

    def test_nochildren(self):
        node1 =  ParentNode(children=[], tag="p")
        self.assertRaises(ValueError, msg="No children")

    def test_notag(self):
        leaf1 = LeafNode(tag="p", value="Hello, world")
        leaf2 = LeafNode(tag="p", value="Goodbye, world")
        node1 =  ParentNode(children=[leaf1, leaf1, leaf2])
        self.assertRaises(ValueError, msg="No tag")

    def test_recursion(self):
        leaf1 = LeafNode(tag="p", value="Hello, world")
        leaf2 = LeafNode(tag="p", value="Goodbye, world")
        node1 =  ParentNode(tag="p", children=[leaf1, leaf2])
        leaf3 = LeafNode(tag="a", value="this link", 
                         props={"href":"https://www.google.com",
                                "target":"_blank"})
        node2 = ParentNode(tag="p", children=[node1, leaf3])

        expected = '<p><p><p>Hello, world</p><p>Goodbye, world</p></p><a href="https://www.google.com" target="_blank">this link</a></p>'
        self.assertEqual(node2.to_html(), expected)





#    def test_props(self):
#
#        node1 = LeafNode(tag="a", value="this link", 
#                         props={"href":"https://www.google.com",
#                                "target":"_blank"})
#        self.assertEqual(node1.props_to_html(), 
#                         ' href="https://www.google.com" target="_blank"')
#    def test_defaults(self):
#        node = LeafNode(value="Hi")
#        self.assertEqual(node.tag, None)
#        self.assertEqual(node.value, "Hi")
#        self.assertEqual(node.props, None)
#        self.assertEqual(node.children, None)
#
#
#    def test_tohtml(self):
#        node1 = LeafNode(tag="a", value="this link", 
#                         props={"href":"https://www.google.com",
#                                "target":"_blank"})
#        self.assertEqual(node1.to_html(), 
#                         '<a href="https://www.google.com" target="_blank">this link</a>')
#







if __name__ == "__main__":
    unittest.main()
