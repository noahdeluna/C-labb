from myheap import Heap

max_heap = Heap(max_heap=True)

with open ('books.txt', 'r') as file:
    for line in file:
        downloads, title = line.rstrip("\n").split(",")
        max_heap.push(int(downloads), title)

k=100
min_heap = Heap(False, k)

with open ('books.txt', 'r') as file:
    for line in file:
        downloads, title = line.rstrip("\n").split(",")
        min_heap.push(int(downloads), title)

