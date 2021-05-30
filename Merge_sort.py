
def merge_sort(data):
    if len(data) < 2:
        return data
    n = len(data)
    mid = n // 2
    ## Devide
    L = merge_sort(data[:mid])
    R = merge_sort(data[mid:])
    ## Merge
    data_sort = []
    i, j = 0, 0
    l, r = len(L), len(R)
    for k in range(l+r):
        if i < l and j < r: ## normal case
            if L[i] > R[j]:
                data_sort += [L[i]]
                i += 1
            elif R[j] > L[i]:
                data_sort += [R[j]]
                j += 1
        elif i == l: ## if L reach end, consider R only
            data_sort += [R[j]]
            j += 1
        elif j == r: ## if R reach end, consider L only
            data_sort += [L[i]]
            i += 1
    return data_sort


if __name__ == '__main__':

    data = [38,14, 57, 59, 52, 19, 1, 2]
    data_sort = merge_sort(data)