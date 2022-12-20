# https://leetcode.com/problems/keys-and-rooms/description/


# first thought, dfs, TC:O(N), SC:O(N)
def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    n = len(rooms)
    visited = set()

    def dfs(node=0):
        if node in visited:
            return False
        visited.add(node)
        if len(visited) == n:
            return True
        for nei in rooms[node]:
            if dfs(nei):
                return True
        return False

    return dfs()