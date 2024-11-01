
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props=props

    def to_html(self):
        raise NotImplementedError

    def __eq__(self, otherNode):
        if self.tag == otherNode.tag:
            if self.value == otherNode.value:
                 if self.children == otherNode.children:
                     if self.props == otherNode.props:
                        return True

        return False

    def props_to_html(self):

        strarr = map(lambda x: f' {x}="{self.props[x]}"', self.props)
        print(strarr)
        return "".join(strarr)


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag=tag, value=value, props=props, children=None)


    def to_html(self):
        if self.value is None:
            raise ValueError

        if self.tag is None:
            return str(self.value)

        if self.props is None:
            prophtml = ""
        else:
            prophtml = self.props_to_html()

        html = f"<{self.tag}{prophtml}>{self.value}</{self.tag}>"
        return html

class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        super().__init__(children=children, tag=tag, props=props, value=None)

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag")
        if len(self.children) == 0 or self.children is None:
            raise ValueError("No children")


        if self.props is None:
            prophtml = ""
        else:
            prophtml = self.props_to_html()

        valuehtml = "".join([s.to_html() for s in self.children])

        html = f"<{self.tag}{prophtml}>{valuehtml}</{self.tag}>"
        return html




