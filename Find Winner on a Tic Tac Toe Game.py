# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/description/

# hashing, TC:O(M) M is len(moves), SC:O(N)
def tictactoe(moves: List[List[int]]) -> str:
    row, col, dia = [0] * 3, [0] * 3, [0] * 2  #
    start = 0 if len(moves) % 2 == 1 else 1
    for i in range(start, len(moves), 2):
        r, c = moves[i]
        if r - c == 0:
            dia[0] += 1
        if r + c == 2:
            dia[1] += 1
        row[r] += 1
        col[c] += 1
        if row[r] == 3 or col[c] == 3 or any(v == 3 for v in dia):
            return "A" if start == 0 else "B"
    if len(moves) == 9: return "Draw"
    return "Pending"