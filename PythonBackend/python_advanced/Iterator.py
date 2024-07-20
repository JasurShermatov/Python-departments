# my_list = [1,2,3,4,5,6,7,8,9]
# # iterable?
# iterator = iter(my_list)
# while True:
#     try:
#         element = next(iterator)
#     except StopIteration:
#         break
#     print(element)



class Counter:
    def __init__(self, count: int):
        self.i = -1
        self.count = count

    def __iter__(self):
        print("got iter call")
        return self

    def __next__(self):
        print("got next call")
        self.i += 1
        if self.i == self.count:
            print("raised StopIteration")
            raise StopIteration
        return self.i


counter = Counter(5)
for c in counter:
    print(c)




# import itertools
# for _ in itertools.count():
#     print("This loop will run forever")


# tuple = ("apple", "banana", "cherry")
# iterator = iter(tuple)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
