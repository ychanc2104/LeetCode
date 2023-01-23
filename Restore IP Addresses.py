# https://leetcode.com/problems/restore-ip-addresses/

# first thought, backtracking, TC:O(N3^N) can separate into N integers and each integer can have 1,2,3 digits(3), SC:O(N)
def restoreIpAddresses(s: str) -> List[str]:
    if len(s) > 12:
        return []
    res = []
    ip = []

    def backtrack(i):
        if i == len(s):
            if len(ip) == 4:
                res.append('.'.join(ip))  # TC:O(N), N integers
            return
        if len(ip) > 4:
            return
        # append new first, and merge if it can be
        ip.append(s[i])  # create new
        backtrack(i + 1)
        ip.pop()
        if ip and ip[-1] != '0' and int(ip[-1]) * 10 + int(s[i]) <= 255:
            # print(ip[-1], ip)
            ip[-1] += s[i]  # TC:O(3) at most
            backtrack(i + 1)

    backtrack(0)
    return res

# backtracking, TC:O(N3^N) can separate into N integers and each integer can have 1,2,3 digits(3), SC:O(N)

def restoreIpAddresses2(s: str) -> List[str]:
    if len(s) > 12:
        return []
    res = []
    ip = []
    def backtrack(i):
        if i == len(s):
            if len(ip) == 4:
                res.append('.'.join(ip)) # TC:O(N), N integers
            return

        for size in range(1,4): # use 1,2,3 digits
            sub = s[i:i+size]
            if (len(sub)>1 and (sub[0] == '0' or int(sub) > 255)) or len(ip) == 4:
                continue
            ip.append(sub)
            backtrack(i+size)
            ip.pop()
    backtrack(0)
    return res