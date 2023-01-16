# https://leetcode.com/problems/maximum-number-of-accepted-invitations/description/

# TC:O(N^2M), SC:O(N+M)
def maximumInvitations(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    memo = {}  # girl: boy

    # if not in memo => assign boy to the girls
    # re-assign girl if the boy no matching

    def dfs(i):
        for g, status in enumerate(grid[i]):
            if status == 0 or g in visited:  # force other boy to choose other girls
                continue
            visited.add(g)  # mark this girl assigned
            if g not in memo or dfs(memo[g]):  # can assign girl to i(boy)
                memo[g] = i
                return True
        return False

    for i in range(n):  # TC:O(N^2M) max
        visited = set()  # attempted assigning girl
        dfs(i) # O(NM)
    return len(memo)