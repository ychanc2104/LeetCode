# https://leetcode.com/problems/isomorphic-strings/description/


#
def isIsomorphic( s: str, t: str) -> bool:
    # no two char map to the same char, ex: b=>a and c=>a
    # should be 1 vs 1 for any char
    memo_st = {}
    memo_ts = {}
    for si, ti in zip(s, t):
        # s map to t
        if si not in memo_st and ti not in memo_ts:
            memo_st[si] = ti
            memo_ts[ti] = si
        else:
            if memo_st.get(si) != ti or memo_ts.get(ti) != si:
                return False
    return True