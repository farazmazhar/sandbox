from time import time


def timer(func):
    def f(*a, **kw):
        before = time()
        rv = func(*a, **kw)
        after = time()

        print('elapsed time:', after - before)

        return rv
    return f


# Higher Order
def ntimes(n):
    def inner(f):
        def wrapper(*args, **kwargs):
            rv = None
            for _ in range(n):
                print('running {.__name__}'.format(f))
                rv = f(*args, **kwargs)
            return rv
        return wrapper
    return inner


@timer
def add(x, y):
    return x + y


if __name__ == "__main__":
    print(add(5, y=2))
