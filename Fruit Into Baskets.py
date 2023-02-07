# https://leetcode.com/problems/fruit-into-baskets/
# https://leetcode.com/problems/fruit-into-baskets/solutions/170740/java-c-python-sliding-window-for-k-elements/


# brute force, TC:O(N^2)
def totalFruit(fruits: List[int]) -> int:
    n = len(fruits)
    res = 1
    for i in range(n):
        first = fruits[i]
        second = None
        count = 1
        for j in range(i + 1, n):
            if second is None:
                if fruits[j] != first:
                    second = fruits[j]
            else:
                if fruits[j] not in (first, second):
                    break
            count += 1
        res = max(res, count)
    return res

# sliding window, TC:O(N), SC:O(N)
def totalFruit2(fruits: List[int]) -> int:
    n = len(fruits)
    # sliding window
    L = 0
    counter = {} # SC:O(1)
    res = 1
    for R in range(n):
        counter[fruits[R]] = counter.get(fruits[R], 0) + 1
        while len(counter) > 2:
            counter[fruits[L]] -= 1
            if counter[fruits[L]] == 0:
                counter.pop(fruits[L])
            L += 1
        res = max(res, R - L + 1)
    return res


# sliding window, TC:O(N), SC:O(1)
def totalFruit3(fruits: List[int]) -> int:
    n = len(fruits)
    # sliding window
    L = 0
    counter = {}
    res = 1
    for R in range(n):
        counter[fruits[R]] = counter.get(fruits[R], 0) + 1
        if len(counter) > 2: # remove one left, no need to contract window
            counter[fruits[L]] -= 1
            if counter[fruits[L]] == 0:
                counter.pop(fruits[L])
            L += 1
        res = max(res, R - L + 1)
    return res