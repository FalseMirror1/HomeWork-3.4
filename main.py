# 1 задание      <<<<---------------------------------------------------------

class FlatIterator:

    def __init__(self, list):
        self.list = [inner for outer in list for inner in outer]

    def __iter__(self):
        self.main_cursor = -1
        return self

    def __next__(self):
        self.main_cursor += 1
        if self.main_cursor == len(self.list):
            raise StopIteration
        return self.list[self.main_cursor]


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    result = FlatIterator(nested_list)
    for item in result:
        print(item)

#  2 задание      <<<<---------------------------------------------------------

    list_gen = (b for a in nested_list for b in a)
    print(list(list_gen))