"""
Cool closures.
"""


def fib():
    x = 0
    y = 1

    def calculate():
        nonlocal x
        nonlocal y

        z = x + y
        x, y = y, z

        return z

    return calculate


if __name__ == "__main__":
    fibonacci = fib()

    for i in range(2, 100):
        print(fibonacci())
