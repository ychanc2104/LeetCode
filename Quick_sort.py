
def quick_sort(data):
    if len(data) <= 1: ## exit
        return data
    pivot = data[0]
    data.remove(pivot)
    L, R = [], []
    for x in data:
        if x < pivot:
            L += [x]
        else:
            R += [x]
    return quick_sort(L) + [pivot] + quick_sort(R)

# in-place, TC:O(nlogn), SC:O(logn)
def quick_sort2(data):
    # move smaller value to L
    def partition(L, R):
        pivot = data[R]
        for i in range(L, R):
            if data[i] <= pivot:
                data[i], data[L] = data[L], data[i]
                L += 1
        data[L], data[R] = data[R], data[L]
        return L
    def helper(L, R):
        if L>=R: return
        pos = partition(L, R)
        helper(L, pos-1)
        helper(pos+1, R)

    helper(0, len(data)-1)



if __name__ == '__main__':

    data = [38,14, 57, 59, 52, 19, 1, 2, 2, 19]
    data_sort = quick_sort(data.copy())

    quick_sort2(data)