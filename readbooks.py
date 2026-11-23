from myheap import Heap
import timeit
import tracemalloc


def max(k,n=75000):
    """
    Koden för alternativ 1
    """
    max_heap = Heap(max_heap=True)
    with open ('books.txt', 'r') as file:
        row=1
        while row<=n:
            line = file.readline()
            downloads, title = line.rstrip("\n").split(",")
            max_heap.push(int(downloads), title)
            row+=1
    topplista = []
    for book in range(k):
        topplista.append(max_heap.pop())
    return topplista

def min(k,n=75000):
    """
    Koden för alternativ 2
    """
    min_heap = Heap(False, k)
    with open ('books.txt', 'r') as file:
        row=1
        while row<=n:
            line = file.readline()
            downloads, title = line.rstrip("\n").split(",")
            min_heap.push(int(downloads), title)
            row+=1
    topplista = []
    for book in range(k):
        topplista.append(min_heap.pop())
    topplista.reverse()
    return topplista

def print_top_books(book_list):
    for book in book_list:
        print(book)

def result(k,n):
    """
    returnerar ifall de två listorna båda har rankat likadant (jämför endast 
    downloads för att ordningen av böcker med samma mängd nedladdningar är ovesentlig)
    """
    top_books = max(k,n)
    bottom_books = min(k,n)
    return [ book.downloads for book in top_books] == [book.downloads for book in bottom_books]

def measure_memory(function, k, n):
        tracemalloc.start()
        result = function(k,n)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        return peak / 1000000  # MB