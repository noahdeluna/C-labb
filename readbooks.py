from myheap import Heap
import timeit


def max(k):
    max_heap = Heap(max_heap=True)
    with open ('books.txt', 'r') as file:
        for line in file:
            downloads, title = line.rstrip("\n").split(",")
            max_heap.push(int(downloads), title)
    topplista = []
    for book in range(k):
        topplista.append(max_heap.pop())
    return topplista

def min(k):
    min_heap = Heap(False, k)
    with open ('books.txt', 'r') as file:
        for line in file:
            downloads, title = line.rstrip("\n").split(",")
            min_heap.push(int(downloads), title)
    topplista = []
    for book in range(k):
        topplista.append(min_heap.pop())
    topplista.reverse()
    return topplista

def print_top_books(book_list):
    for book in book_list:
        print(book)

def result(k):
    print("Alternativ 1:")
    top_books = max(k)
    print_top_books(top_books)
    print("Alternativ 2:")
    bottom_books = min(k)
    print_top_books(bottom_books)


if __name__ == "__main__":
    k= 10
    result(k)
    

    bintid = timeit.timeit(stmt = lambda: max(k), number = 100)
    print(f"Alternativ 1 där n = 75000 och k = {k} tog", round(bintid, 4) , "sekunder")

    bintid = timeit.timeit(stmt = lambda: min(k), number = 100)
    print(f"Alternativ 2 där n = 75000 och k = {k} tog", round(bintid, 4) , "sekunder")