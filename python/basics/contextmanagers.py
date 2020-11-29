"""
Context Managers in Pyhton.
"""

from contextlib import contextmanager


class One:
    def __init__(self, path: str) -> None:
        self.file = open(file=path, mode='r+')

    def __enter__(self):
        print(self.file.readlines())

    def __exit__(self, *args):
        print(args)
        self.file.close()


# with One('contextmanagers.py') as f:
    # print('Reading file lines...')

@contextmanager
def two(path: str):
    f = open(path, 'r')

    try:
        yield f.readlines()
    finally:
        f.close()


with two('contextmanagers.py') as f:
    for line in f:
        print(line.strip())
