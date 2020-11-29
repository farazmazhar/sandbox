"""
Magic Methods in Python.
"""

from typing import Any


class Magic:
    def __init__(self, cool: list) -> None:
        self.cool = cool

    # TODO Understand __new__ method.
    # def __new__(cls, *args) -> Any:
    #     print('New object...')
    #     print(cls)
    #     print(args)
    #     return cls

    # TODO Understand __call__ method.
    # def __call__(self, *args: Any, **kwds: Any) -> Any:
    #     print('call...')
    #     print(args)
    #     print(kwds)

    def __setitem__(self, item: int, value: Any) -> None:
        self.cool[item] = value

    def __getitem__(self, item: int) -> Any:
        return '*' * self.cool[item]

    def __delitem__(self, item: int) -> None:
        del self.cool[item]

    def __iter__(self):
        for item in self.cool:
            yield item

    def __str__(self) -> str:
        return str(self.cool)

    def __eq__(self, o: object) -> list:
        return list(map(lambda x, y: x == y, self, o))

    def __ne__(self, o: object) -> list:
        return list(map(lambda x, y: x != y, self, o))


def magic_demo():
    m = Magic([1, 2, 3, 4, 5, 6])
    n = Magic([1, 2, 3, 4, 5, 6])

    m[2] = 7
    del m[3]
    print(m[2])
    print(m)

    for i in m:
        print('+' * i)

    print(m == n)
    print(m != n)


class CoolArray:
    def __init__(self, size: int, type: type) -> None:
        self.size = size
        self.array = [None] * size
        self.type = type

    def _is_index_proper(self, index) -> bool:
        """
        Determines wether the index was inside the size or not.
        """
        return index >= 0 and index < self.size

    def __setitem__(self, index, value) -> None:
        if isinstance(value, self.type) and self._is_index_proper(index):
            self.array[index] = value
        else:
            raise Exception('Index out of bounds.')

    def __getitem__(self, index) -> Any:
        if self._is_index_proper(index):
            return self.array[index]
        else:
            raise Exception('Index out of bounds.')

    def __delitem__(self, index) -> None:
        if self._is_index_proper(index):
            del self.array[index]
        else:
            raise Exception('Index out of bounds.')

    def __init__(self) -> Any:
        for item in self.array:
            yield item

    def __add__(self, o: object) -> list:
        return list(map(lambda x, y: x + y), self, o)

    def __sub__(self, o: object) -> list:
        return list(map(lambda x, y: x - y), self, o)

    def __mul__(self, o: object) -> list:
        return list(map(lambda x, y: x * y), self, o)

    def __div__(self, o: object) -> list:
        return list(map(lambda x, y: x / y), self, o)

    def __mod__(self, o: object) -> list:
        return list(map(lambda x, y: x % y), self, o)

    def __eq__(self, o: object) -> list:
        return list(map(lambda x, y: x == y), self, o)

    def __ne__(self, o: object) -> list:
        return list(map(lambda x, y: x != y), self, o)

    def __gt__(self, o: object) -> list:
        return list(map(lambda x, y: x > y), self, o)

    def __lt__(self, o: object) -> list:
        return list(map(lambda x, y: x < y), self, o)

    def __ge__(self, o: object) -> list:
        return list(map(lambda x, y: x >= y), self, o)

    def __le__(self, o: object) -> list:
        return list(map(lambda x, y: x <= y), self, o)




if __name__ == "__main__":
    one = CoolArray(size=10, type=int)
    two = CoolArray(size=10, type=int)

    print(one == two)
