

def swap(data, i, j):
    data[i], data[j] = data[j], data[i]
    return data

def max_root(data):
    n = len(data)
    return n//2-1

def heapify(data, n, i):
    if i >= n:
        return None
    max = i
    c1 = 2*i + 1
    c2 = 2*i + 2
    if c1 < n:
        if data[c1] >= data[max]:
            max = c1
    if c2 < n:
        if data[c2] > data[max]:
            max = c2
    if max != i:
        swap(data, i, max)
        heapify(data, n, max)

def max_heapify(data):
    n = len(data)
    roots = max_root(data)
    for i in range(roots+1):
        heapify(data, n, roots-i)

def heap_sort(data):
    data_sort = []
    data_copy = data.copy()
    for i in range(len(data_copy)):
        max_heapify(data_copy)
        swap(data_copy, 0, -1)
        data_sort += [data_copy[-1]]
        data_copy.remove(data_copy[-1])
    return data_sort



if __name__ == '__main__':

    data = [38,14, 57, 59, 52, 19]
    # data = [4, 2, 3, 5, 1, 10]

    data_sort = heap_sort(data)
