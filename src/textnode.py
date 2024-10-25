from enum import Enum

class TextType(Enum):
    NORMAL = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = 5
    IMAGE = 6


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, otherNode):
        return self.text == (otherNode.text and
            self.text_type == otherNode.text_type and 
            self.url == otherNode.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

