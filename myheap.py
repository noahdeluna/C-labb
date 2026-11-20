class Book:
    def __init__(self, downloads, name):
        self.name = name
        self.downloads = downloads

    def __str__(self):
        return f"Title: {self.name}, Downloads: {self.downloads}"

class Heap:
    def __init__(self, max_heap=True, max_size = 9999999999):
            self.items = []
            self.max_heap = max_heap
            self.max_size = max_size

    def __len__(self):
            return len(self.items)

    def _higher_priority(self, a, b):
            if self.max_heap:
                return a.downloads > b.downloads
            return a.downloads < b.downloads

    def push(self, downloads, name):
            if not self.max_heap and len(self.items) == self.max_size:
                if downloads <= self.items[0].downloads:
                    return
                else:
                    self.pop()
            self.items.append(Book(downloads,name))
            child = len(self.items) - 1
            while child > 0:
                parent = (child - 1) // 2
                if not self._higher_priority(self.items[child], self.items[parent]):
                    break
                self.items[child], self.items[parent] = self.items[parent], self.items[child]
                child = parent
            

    def peek(self):
            if not self.items:
                raise IndexError("peek from empty heap")
            return self.items[0]

    def pop(self):
            if not self.items:
                raise IndexError("pop from empty heap")
            root = self.items[0]
            last = self.items.pop()
            if self.items:
                self.items[0] = last
                parent = 0
                while True:
                    left = 2 * parent + 1
                    right = left + 1
                    best = parent
                    if left < len(self.items) and self._higher_priority(self.items[left], self.items[best]):
                        best = left
                    if right < len(self.items) and self._higher_priority(self.items[right], self.items[best]):
                        best = right
                    if best == parent:
                        break
                    self.items[parent], self.items[best] = self.items[best], self.items[parent]
                    parent = best
            return root

    