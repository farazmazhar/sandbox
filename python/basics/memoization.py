import timeit
import sys
from functools import lru_cache


# No memoization
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Custom memoization
fibonacci_cache = {}


def fibonacci_cached(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 1 or n == 2:
        value = 1
    else:
        value = fibonacci_cached(n-1) + fibonacci_cached(n-2)

    fibonacci_cache[n] = value
    return value


# LRU cached memoization
@lru_cache()
def fibonacci_lru(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_lru(n-1) + fibonacci_lru(n-2)


def loop_many_times(func):
    for i in range(1, 1001):
        value = func(i)
        # print(str(i) + ':', value)


if __name__ == "__main__":
    # print('Timing non-memozied function:')
    # print(timeit.timeit("fibonacci(35)", "from __main__ import fibonacci", number=1))
    # # print(timeit.timeit(loop_many_times(fibonacci), number=1))

    # print('Timing custom memozied function:')
    # print(timeit.timeit("fibonacci_cached(1000)",
    #                     "from __main__ import fibonacci_cached, fibonacci_cache", number=1))
    # print(timeit.timeit("loop_many_times(fibonacci_cached)",
    #                     "from __main__ import loop_many_times, fibonacci_cached, fibonacci_cache", number=1))

    # sys.setrecursionlimit(1500)
    # print('Timing lru memozied function:')
    # print(timeit.timeit("fibonacci_lru(1000)",
    #                     "from __main__ import fibonacci_lru", number=1))
    print(timeit.timeit("loop_many_times(fibonacci_lru)",
                        "from __main__ import loop_many_times, fibonacci_lru", number=1))

