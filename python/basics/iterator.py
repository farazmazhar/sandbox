# Iterators iterate values.

# Concept
nums = [7, 8, 9, 5]

it = iter(nums)

if next(it):
    print(next(it))

# Example

class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num  <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values  = TopTen()

print(next(values))

for i in values: # Will call __next__ under the hood.
    print(i)


        