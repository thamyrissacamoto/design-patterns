class Iterator:
    def __init__(self, aggregate):
        self._aggregate = aggregate
        self._index = 0

    def has_next(self):
        return self._index < len(self._aggregate)

    def next(self):
        if self.has_next():
            item = self._aggregate[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

class Aggregate:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def create_iterator(self):
        return Iterator(self._items)

aggregate = Aggregate()
aggregate.add_item("Item 1")
aggregate.add_item("Item 2")
aggregate.add_item("Item 3")

iterator = aggregate.create_iterator()

while iterator.has_next():
    print(iterator.next())
