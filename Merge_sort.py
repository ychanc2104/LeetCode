def MergeSort(data):
    if len(data) < 2:
        return data
    n = len(data)
    mid = n // 2
    ## Devide
    L = MergeSort(data[:mid])
    R = MergeSort(data[mid:])
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
        print(data_sort)
    return data_sort



data = [38,14, 57, 59, 52, 19, 1, 2]
data_sort = MergeSort(data)