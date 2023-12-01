import os

def read_file(fname):
    if not fname.endswith('.txt'):
        fname += '.txt'
    path = os.path.realpath(__file__)
    dir = os.path.dirname(path)
    dir = dir.replace('days', 'resources')
    os.chdir(dir)
    file = open(fname)
    content = file.readlines()
    file.close()
    return content