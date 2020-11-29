# Generators give iterators.

# Concept
def toptenperfectsquares():
    n = 1

    while n <= 10:
        sq = n*n
        yield sq
        n += 1

prefectsq = toptenperfectsquares()

for i in prefectsq:
    print(i)


# Example
