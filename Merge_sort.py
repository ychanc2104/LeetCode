## divide and conquer
import collections


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

def merge(data_L, data_R):

    data_L = collections.deque(data_L)
    data_R = collections.deque(data_R)
    data_merge = []
    while data_L and data_R:
        if data_L[0] < data_R[0]:
            data_merge.append(data_L.popleft())
            # data_merge.append(data_L.pop(0))

        else:
            data_merge.append(data_R.popleft())
            # data_merge.append(data_R.pop(0))
    # return data_merge + data_L if data_L else data_merge + data_R
    return data_merge + list(data_L) if data_L else data_merge + list(data_R)


def merge_sort2(data):
    if len(data) <= 1:
        return data
    n = len(data)
    mid = n // 2
    ## Devide
    L = merge_sort2(data[:mid])
    R = merge_sort2(data[mid:])
    ## Merge
    return merge(L, R)



if __name__ == '__main__':

    data = [38,14, 57, 59, 52, 19, 1, 2]
    data_sort = merge_sort(data)
    data_sort2 = merge_sort2(data)