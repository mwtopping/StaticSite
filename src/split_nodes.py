from textnode import TextType, TextNode, text_node_to_html_node
from htmlnode import HTMLNode
from extract_markdown import extract_markdown_links, extract_markdown_images




def split_nodes_delimiter(old_nodes, delimiter, text_type):

    output_nodes = []
    for node in old_nodes:
        if text_type == node.text_type:
            output_nodes.append(node)
            continue
        nodetext = node.text
        splittext = nodetext.split(delimiter)
        if len(splittext) % 2 == 0:
            raise Exception("Not valid markdown, missing delimiter somewhere")
        delimited = False
        for t in splittext:
            if not delimited:
                delimited = True
                newnode = TextNode(t, node.text_type)
            else:
                delimited= False
                newnode = TextNode(t, text_type)
            output_nodes.append(newnode)

    return output_nodes


def split_nodes_images(nodes):
    newnodes = []

    for node in nodes:
        linkpairs = extract_markdown_images(node.text)
        if len(linkpairs) == 0:
            newnodes.append(node)
            continue
        workingtext = node.text
        for pair in linkpairs:
            splittext = workingtext.split(f"![{pair[0]}]({pair[1]})")
            pretext = splittext[0]
            workingtext = splittext[-1]
            if len(pretext.replace(' ', '')) > 0:
                newnodes.append(TextNode(pretext, TextType.TEXT))
            newnodes.append(TextNode(pair[0], TextType.IMAGE, url=pair[1]))
    
        newnodes.append(TextNode(workingtext, TextType.TEXT))
    return newnodes



def split_nodes_links(nodes):
    newnodes = []

    for node in nodes:
        linkpairs = extract_markdown_links(node.text)
        if len(linkpairs) == 0:
            newnodes.append(node)
            continue
        workingtext = node.text
        for pair in linkpairs:
            splittext = workingtext.split(f"[{pair[0]}]({pair[1]})")
            pretext = splittext[0]
            workingtext = splittext[-1]
            if len(pretext.replace(' ', '')) > 0:
                newnodes.append(TextNode(pretext, TextType.TEXT))
            newnodes.append(TextNode(pair[0], TextType.LINK, url=pair[1]))
    return newnodes





def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    nodes = [node]
    newnodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
    newnodes = split_nodes_delimiter(newnodes, '*', TextType.ITALIC)
    newnodes = split_nodes_delimiter(newnodes, '`', TextType.CODE)
    newnodes = split_nodes_images(newnodes)
    newnodes = split_nodes_links(newnodes)
    return newnodes





def markdown_to_blocks(mdown):

    lines = mdown.split('\n\n')
    strippedlines = []
    for line in lines:
        line = line.strip()
        if len(line) > 0:
            strippedlines.append(line)

    return lines




def block_to_block_type(block):

    if block[0] == '#':
        return ("heading", block.lstrip('#'))
    if block[0:3] == "```" and block[-3:] == "```":
        return ("code", block.strip('`'))
    if all([l[0]==">" for l in block.split('\n')]):
        return ("quote", [l.lstrip('>') for l in block.split('\n')])
    if all([l[0:2] in ["* ", "- "] for l in block.split('\n')]):
        return ("unordered_list", [l.lstrip('*-') for l in block.split('\n')])

    ol_expected = "".join([l[0:2] for l in block.split('\n')])
    ol_actual = "".join([f"{ii+1}." for ii in range(len(block.split('\n')))])
    if ol_actual == ol_expected:
        return ("ordered_list", block.split('\n'))
    return ("paragraph", block)




def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    blocknodes = []

    #def __init__(self, tag=None, value=None, children=None, props=None):
    for block in blocks:
        blocktype, blocktexts = block_to_block_type(block)
        htmlnodes = []
        subtag = None
        match blocktype:
            case "heading":
                tag = "h1"
                nodes = text_to_textnodes(blocktexts)
                htmlnodes = text_node_to_html_node(nodes)
                htmlnodes = HTMLNode(tag=tag, value=None, children=nodes, props=None)
            case "code":
                tag = "pre"
                subtag = "code"
                if isinstance(blocktexts, list):
                    nodes = []
                    for t in blocktexts:
                        nodes.extend(text_to_textnodes(t))
                else:
                    nodes = text_to_textnodes(blocktexts)

                htmlnodes = text_node_to_html_node(nodes)
                # wrap the code block in pre tags
                htmlnodes = HTMLNode(tag='code', value=None, children=htmlnodes, props=None)
                htmlnodes = HTMLNode(tag='pre', value=None, children=htmlnodes, props=None)
            case "quote":
                tag = "blockquote"
                nodes = text_to_textnodes(blocktexts)
                htmlnodes = text_node_to_html_node(nodes)
                htmlnodes = HTMLNode(tag=tag, value=None, children=nodes, props=None)
            case "unordered_list":
                tag = "ul"
                subtag = "li"
                nodes = text_to_textnodes(blocktexts)
                htmlnodes = text_node_to_html_node(nodes)
                htmlnodes = HTMLNode(tag=subtag, value=None, children=nodes, props=None)
                htmlnodes = HTMLNode(tag=tag, value=None, children=nodes, props=None)
            case "ordered_list":
                tag = "ol"
                subtag = "li"
                nodes = text_to_textnodes(blocktexts)
                htmlnodes = text_node_to_html_node(nodes)
                htmlnodes = HTMLNode(tag=subtag, value=None, children=nodes, props=None)
                htmlnodes = HTMLNode(tag=tag, value=None, children=nodes, props=None)
            case "paragraph":
                tag = "p"
                nodes = text_to_textnodes(blocktexts)
                htmlnodes = text_node_to_html_node(nodes)
                htmlnodes = HTMLNode(tag=tag, value=None, children=nodes, props=None)
            case _:
                tag = None

        if len(htmlnodes) > 0:
            blocknodes.append(htmlnodes)        

    finalhtmlnode = HTMLNode(tag="div", value=None, children=blocknodes)
#    new_htmlblock = HTMLNode(tag, value, children=children, props)
    return finalhtmlnode




if __name__ == "__main__":
    text = "1. Test, this stuff\n2.  ol2\n3.  ol3"
    result = block_to_block_type(text)
    print(result)

