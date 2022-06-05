# https://leetcode.com/problems/counting-bits/
# https://leetcode.com/problems/counting-bits/discuss/79539/Three-Line-Java-Solution
#

# first thought
def countBits(n: int):
    res = []
    for i in range(n + 1):
        ans = 0
        while i > 0:
            ans += i & 1
            i = i >> 1
        res.append(ans)
    return res

## recurrence relation
"""
f[1] = (f[0]==0) + (1%1==1) = 1
f[11] = (f[1]==1) + (11%1==1)  = 2
f[110] = (f[11]==2) + (110%1==0) = 2
f[1101] = (f[110] ==2) + (1101%1==1) =3;
"""
def countBits2(n: int):
    res = [0]
    for i in range(1,n+1):
        #print(i, i>>1)
        res.append(res[i>>1]+(i&1))
    return res