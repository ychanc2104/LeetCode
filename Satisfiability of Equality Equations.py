# https://leetcode.com/problems/satisfiability-of-equality-equations/?envType=study-plan&id=graph-ii


# first thought union find, TC:O(N*alpha(26))~O(N), TC:O(26)~O(1)
def equationsPossible(equations: List[str]) -> bool:
    # '==' connect a and b
    # '!=' if pa == pb return False
    # union '==' first
    parents = [i for i in range(26)]

    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    for eq in equations:
        if eq[1] == '!': continue  # skip '!='
        a = ord('a') - ord(eq[0])
        b = ord('a') - ord(eq[-1])
        pa, pb = find(a), find(b)
        parents[pa] = pb
    for eq in equations:
        if eq[1] == '=': continue  # skip '=='
        a = ord('a') - ord(eq[0])
        b = ord('a') - ord(eq[-1])
        pa, pb = find(a), find(b)
        if pa == pb:
            return False
    return True