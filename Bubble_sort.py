
def bubble_sort(data):
    n = len(data)
    data_copy = data.copy()
    for i in range(n):
        for j in range(n-i-1):
            if data_copy[j] > data_copy[j+1]:
                data_copy[j], data_copy[j+1] = data_copy[j+1], data_copy[j]
    return data_copy


if __name__ == '__main__':

    data = [38,14, 57, 59, 52, 19, 1, 2]
    data_sort = bubble_sort(data)