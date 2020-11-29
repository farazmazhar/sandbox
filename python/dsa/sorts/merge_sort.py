"""
Merge... merge... merge...
"""

import random
from time import time
from contextlib import contextmanager


@contextmanager
def timeit():
    start = time()

    try:
        yield
    finally:
        end = time()

        print('total time:', end - start)


def merge_sort(array: list) -> list:
    # print(len(array), array)
    if len(array) == 1:
        return array
    else:
        array_one = merge_sort(array[:len(array) // 2])
        array_two = merge_sort(array[len(array) // 2:])

        print(array_one, array_two)
        return merge(array_one, array_two)


def merge(array_one: list, array_two: list) -> list:
    array_three = []

    while array_one and array_two:
        if array_one[0] > array_two[0]:
            array_three.append(array_two[0])
            del array_two[0]
        else:
            array_three.append(array_one[0])
            del array_one[0]

    array_three += array_one
    array_three += array_two

    return array_three


if __name__ == "__main__":
    big_list = []

    # for i in range(100000):
    #     big_list.append(random.random() * 10)

    big_list = [2, 5, 3, 1, 8, 9, 7, 4, 6]

    with timeit():
        final = merge_sort(big_list)
        print(final)

    with timeit():
        l = big_list
        l.sort()
        print(l)
