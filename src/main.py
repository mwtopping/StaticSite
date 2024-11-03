from textnode import TextType, TextNode
from extract_markdown import extract_title
from split_nodes import markdown_to_html_node
import shutil
import os



def copy_site(source, dest):
    sources, destinations, directories = get_moves("./static", "./public")
    print("Building Tree")
    print(directories)
    if os.path.isdir(dest):
        shutil.rmtree(dest)
    os.mkdir(dest) 
    for d in directories:
        os.mkdir(d)
    for s, d in zip(sources, destinations):
        print(f"{s} -> {d}")
        shutil.copy(s, d)


def get_moves(source, dest):

    sources = []
    destinations = []
    directories = []
    # get list of source files
    files = os.listdir(source)
    for f in files:
        if os.path.isdir(f"{source}/{f}"):
            directories.append(f"{dest}/{f}")
            ss, ds, drs = get_moves(f"{source}/{f}", f"{dest}/{f}")
            sources.extend(ss)
            destinations.extend(ds)
            directories.extend(drs)
        else:
            sources.append(f"{source}/{f}")
            destinations.append(f"{dest}/{f}")

    
    return sources, destinations, directories



def get_pages_to_create(dir_path_content, template_path, dest_dir_path):
    page_sources = []
    page_dests = []
    files = os.listdir(dir_path_content)
    for f in files:
        if os.path.isdir(f"{dir_path_content}/{f}"):
            sources, dests = get_pages_to_create(f"{dir_path_content}/{f}", 
                                                 template_path,
                                                 f"{dest_dir_path}/{f}")
            page_sources.extend(sources)
            page_dests.extend(dests)
        else:
            page_sources.append(f"{dir_path_content}/{f}")
            page_dests.append(f"{dest_dir_path}/{f.replace('.md', '.html')}")

    return page_sources, page_dests


def generate_all_pages(dir_path_content, template_path, dest_dir_path):
    sources, dests = get_pages_to_create(dir_path_content, template_path, dest_dir_path)
    for s, d in zip(sources, dests):
        generate_page(s, template_path, d)



def generate_page(from_path, template_path, dest_path):
    with open(from_path, 'r') as f:
        input_md = f.read()
    with open(template_path, 'r') as f:
        template = f.read()

    title = extract_title(input_md).strip()
    html = markdown_to_html_node(input_md).to_html()

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    # TODO make directory tree to dest_path if not exists
    if not os.path.isdir("/".join(dest_path.split('/')[:-1])):
        os.mkdir("/".join(dest_path.split('/')[:-1]))

    print(dest_path)
    print("Making ", "/".join(dest_path.split('/')[:-1]))

    with open(dest_path, 'w') as f:
        f.write(template)


def main():
#    generate_page("./content/index.md", "template.html", "./public/index.html")
    copy_site("./static", "./public")
    generate_all_pages("./content", "template.html", "./public")


if __name__ == "__main__":
    main()
