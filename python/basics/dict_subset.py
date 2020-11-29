"""
How to figure out if a dict is a subset of another dict?
"""

a = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6
}

b = {
    'a': 1,
    'b': 2,
    'c': 3
}


if __name__ == "__main__":
    print('b in a:', set(b.items()).issubset(set(a.items())))
    print('another one:', a.items() >= b.items())
    
    print('a on b:', set(a.items()).issuperset(set(b.items())))
