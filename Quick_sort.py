
def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    data.remove(pivot)
    L, R = [], []
    for x in data:
        if x < pivot:
            L += [x]
        elif x > pivot:
            R += [x]
    return quick_sort(L) + [pivot] + quick_sort(R)

if __name__ == '__main__':

    data = [38,14, 57, 59, 52, 19, 1, 2]
    data_sort = quick_sort(data)