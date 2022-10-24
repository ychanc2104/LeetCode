# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/


# first thought, TC:O(M*2^N), SC:O(N)
def maxLength(arr: List[str]) -> int:
    n = len(arr)
    arr_list = [list(s) for s in arr]
    res = [0]

    def helper(pos=0, path=[]):
        if pos == n:
            if len(path) < res[0]:
                return
            # check valid
            if len(path) == len(set(path)):
                res[0] = max(res[0], len(path))
            return
        helper(pos + 1, path + arr_list[pos])  # choose
        helper(pos + 1, path)  # not choose

    helper()  # TC:O(2^N)
    return res[0]

def maxLength2(arr: List[str]) -> int:
    n = len(arr)

    def isOverlap(s1, s2):
        s_concat = s1 + s2
        return len(s_concat) > len(set(s_concat))

    def helper(pos=0, path=''):
        if pos == n:
            return len(path)
            # check valid
        res = 0
        if not isOverlap(path, arr[pos]):  # valid
            res = helper(pos + 1, path + arr[pos])
        return max(res, helper(pos + 1, path))  # choose and not choose
    return helper()


# backtracking, TC:O(M*2^N), SC:O(N) for recursion calls
def maxLength3(arr: List[str]) -> int:
    n = len(arr)
    arr_list = [list(s) for s in arr]
    def helper(pos=0, path=[]):
        # check valid
        if len(path) != len(set(path)): # not valid
            return 0
        if pos == n: # valid, only check 2^N states
            return len(path)
        return max(helper(pos + 1, path + arr_list[pos]), helper(pos + 1, path))
    return helper()


# bit
def maxLength4(arr: List[str]) -> int:
    dp = [set()]
    for a in arr:
        if len(set(a)) < len(a): continue
        a = set(a)
        for c in dp[:]:
            if a & c: continue
            dp.append(a | c)
    return max(len(a) for a in dp)