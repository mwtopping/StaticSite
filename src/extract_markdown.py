import re




def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_title(markdown):
    matches = re.findall(r"\# (.*?)\n", markdown)
    title = matches[0]
    return title



if __name__ == "__main__":


    with open('../content/index.md', 'r') as f:
        markdown = f.read()

    extract_title(markdown)


