import os

path = "/Users/nick/python/labs/DirTree/test"


def dtg(path):
    for root, directory, files in os.walk(path):
        for item in files:
            print(root + item)

dtg(path)





