from textnode import TextType, TextNode
import os



def copy_site(source, dest):
    sources, destinations, directories = get_moves("../static", "../public")
    print("Building Tree")
    print(directories)
    for s, d in zip(sources, destinations):
        print(f"{s} -> {d}")



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






def main():
    copy_site("../static", "../public")


if __name__ == "__main__":
    main()
