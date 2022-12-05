# https://leetcode.com/problems/swap-adjacent-in-lr-string/description/

# TC:O(N), SC:O(1)
def canTransform(start: str, end: str) -> bool:
    S, E, n = 0, 0, len(start)
    # S or L 'R' or 'L'
    while S < n or E < n:
        if S < n and start[S] == 'X':
            S += 1
            continue
        if E < n and end[E] == 'X':
            E += 1
            continue
        if S < n and E < n and start[S] == 'R' and end[E] == 'R' and S <= E:
            S += 1
            E += 1
            continue
        elif S < n and E < n and start[S] == 'L' and end[E] == 'L' and S >= E:
            S += 1
            E += 1
            continue
        return False
    return True