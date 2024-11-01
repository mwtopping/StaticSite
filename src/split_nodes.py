from textnode import TextType, TextNode




def split_nodes_delimiter(old_nodes, delimiter, text_type):

    if text_type == TextType.TEXT:
        return old_nodes

    output_nodes = []

    for node in old_nodes:
        nodetext = node.text
        splittext = nodetext.split(delimiter)
        if len(splittext) % 2 == 0:
            raise Exception("Not valid markdown, missing delimiter somewhere")
        delimited = False
        for t in splittext:
            if not delimited:
                delimited = True
                newnode = TextNode(t, TextType.TEXT)
            else:
                delimited= False
                newnode = TextNode(t, text_type)
            output_nodes.append(newnode)

        return output_nodes


if __name__ == "__main__":
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    
