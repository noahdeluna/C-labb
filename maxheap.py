"""Binary-heap solutions for finding the k most-downloaded books.

Book records are dictionaries with `title` and `downloads` keys.
This implementation is AI-generated and should be identified as such if used,
in accordance with the course instructions provided with the assignment.
"""


class BinaryHeap:
    """Array-based binary heap; `max_heap=True` gives highest priority to larger keys."""

    def __init__(self, max_heap=True):
        self.items = []
        self.max_heap = max_heap

    def __len__(self):
        return len(self.items)

    def _higher_priority(self, a, b):
        if self.max_heap:
            return a[0] > b[0]
        return a[0] < b[0]

    def push(self, priority, value):
        self.items.append((priority, value))
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


def top_k_max_heap(books, k):
    """Insert all books into a max-heap, then remove the best k."""
    if k < 0:
        raise ValueError("k must be non-negative")
    heap = BinaryHeap(max_heap=True)
    for book in books:
        heap.push(book["downloads"], book)
    result = []
    for _ in range(min(k, len(heap))):
        result.append(heap.pop()[1])
    return result


def top_k_bounded_min_heap(books, k):
    """Keep only the best k books in a min-heap of capacity k."""
    if k < 0:
        raise ValueError("k must be non-negative")
    if k == 0:
        return []

    heap = BinaryHeap(max_heap=False)
    for book in books:
        downloads = book["downloads"]
        if len(heap) < k:
            heap.push(downloads, book)
        elif downloads > heap.peek()[0]:
            heap.pop()
            heap.push(downloads, book)

    # Pop gives ascending order from a min-heap, so reverse to return descending.
    result = [heap.pop()[1] for _ in range(len(heap))]
    result.reverse()
    return result
