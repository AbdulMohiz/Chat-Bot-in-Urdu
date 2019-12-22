# It finds all the files in a folder and returns a list of all those files.
# Author  : Syed Awais Kazmi
# COMSATS : SP15-R01-009

# Store all the file names of a folder
# in a list and return this list to the caller

from os import walk


def files_in_folder(corpus_path):
    f = []
    for (dirpath, dirnames, filenames) in walk(corpus_path):
        f.extend(filenames)
        break
    return f



