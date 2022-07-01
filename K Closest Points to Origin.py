# https://leetcode.com/problems/k-closest-points-to-origin/
# https://leetcode.com/problems/k-closest-points-to-origin/discuss/1647773/C%2B%2BPython-Simple-Solutions-w-Explanation-or-Sort-%2B-Heap-%2B-Randomized-QuickSelect-O(N)

import heapq, random

# first thought, sort by custom key, TC:O(NlogN), SC:O(N) for timsort
def kClosest(points, k):
    return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:k]


# using heap queue, TC:O(Nlogk), SC:O(N)
def kClosest2(points, k):
    heap = []
    # push all (distance, (point)) to the heap
    for x,y in points:
        if len(heap)>=k:
            heapq.heappushpop(heap, (-x**2-y**2,(x,y)))
        else:
            heapq.heappush(heap, (-x**2-y**2,(x,y)))
    return [x[1] for x in heap]


# put all points that smaller than kth smallest distant to the leftmost
# using quick select, TC:O(N) average, SC:O(1)
def kClosest3(points, k):
    dis = lambda x: x[0] ** 2 + x[1] ** 2
    # partition from [L,R]
    def partition(L, R):
        # move to bigger distant to the right
        i_pivot = random.randint(L, R)  # prevent drop into worst case
        dis_pivot = dis(points[i_pivot])
        # move pivot to the rightmost to prevent swapping
        points[i_pivot], points[R] = points[R], points[i_pivot]
        # partition all point for L to R-1 according to dis_pivot
        for i in range(L, R):
            # move all point is smaller than dis_pivot to the L
            if dis(points[i]) <= dis_pivot:
                points[i], points[L] = points[L], points[i]
                L += 1
        # L is not partitioned yet, swap pivot to L
        points[L], points[R] = points[R], points[L]
        # return points[:L] is ok, return range [L,R]
        return L
    L, R = 0, len(points) - 1
    # points[L] must >= all point [0,L-1]
    # L and R converge to k
    while L < R: # or L < k is more readable
        i_pivot = partition(L, R)
        if i_pivot > k:
            # move R to left
            R = i_pivot - 1  # no need to sort again
        #elif i_pivot == k: # not required
            #break
        else:
            # move L to right
            L = i_pivot + 1
    return points[:k]