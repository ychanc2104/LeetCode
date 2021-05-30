import random
import time
from Heap_sort import heap_sort
from Heap_sort_2 import heapSort as heap_sort2

from Merge_sort import merge_sort
from Quick_sort import quick_sort
from Bubble_sort import bubble_sort


n = 500
data = [random.random() for i in range(n)]

t1 = time.time()
merge = bubble_sort(data)
t2 = time.time()
print(f'bubble sort spent time {t2-t1} s')

t1 = time.time()
heap = heap_sort(data)
t2 = time.time()
print(f'heap sort spent time {t2-t1} s')

t1 = time.time()
heap = heap_sort2(data)
t2 = time.time()
print(f'heap sort_2 spent time {t2-t1} s')

t1 = time.time()
merge = merge_sort(data)
t2 = time.time()
print(f'merge sort spent time {t2-t1} s')

t1 = time.time()
quick = quick_sort(data)
t2 = time.time()
print(f'quick sort spent time {t2-t1} s')