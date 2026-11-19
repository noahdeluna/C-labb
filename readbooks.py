import maxheap as mh

maxheap = mh.BinaryHeap()
with open ('books.txt', 'r') as file:
    books = file.readlines()
    for line in books:
        line_list = line.strip().split(",")
        print(line_list)
        maxheap.push(int(line_list[0]), line_list[1])

print(maxheap.peek())