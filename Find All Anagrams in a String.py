# https://leetcode.com/problems/find-all-anagrams-in-a-string/

# get all permutations
def get_anagrams(p):
    res = []

    def dfs(pos):
        if pos == len(p):
            res.append(''.join(p))
        for i in range(pos, len(p)):
            print(pos, i)
            p[i], p[pos] = p[pos], p[i]
            dfs(pos+1)
            p[i], p[pos] = p[pos], p[i]
    dfs(0)
    return res


p = list('abc')

res = get_anagrams(p)
