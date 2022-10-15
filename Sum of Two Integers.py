# https://leetcode.com/problems/sum-of-two-integers/
# https://leetcode.com/problems/sum-of-two-integers/discuss/776952/Python-BEST-LeetCode-371-Explanation-for-Python
# 2's complement https://zh.wikipedia.org/wiki/%E4%BA%8C%E8%A3%9C%E6%95%B8, same operation with positive number

# simple java ver., valid for a,b > 0 in python
def getSum(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return getSum(a^b, (a&b)<<1)


# python ver., should add mask
# -1 & 0xff = 255, -2 & 0xff = 254 (-128 to 127)
# 11111111 => -1, 11111110 => -2 ..., 10000000 => -128
# -1000 <= a, b <= 1000
# ~(x+1)+1 = ~x, ~0b1001 = -10, actually is 5 bit,
def getSum2(a: int, b: int) -> int:
    mask = 0xffffffff # 32 bits
    a = a & mask # keep only last 32 bits
    while b:
        s = (a ^ b) & mask
        carry = ((a & b) << 1) & mask
        a = s
        b = carry

    if (a >> 31) & 1:  # If a is negative in 32 bits sense
        # if (a >> 31) == 1, a must be a negative number
        # a ^ mask => make first bit to 0 (sign bit)
        # ~x => get complement of x
        return ~(a ^ mask) # use ~ to make 'a' negative, add - at first bit => become 33 bit
    return a

"""
-1 + 2 (4 bit)
 1111 (-1)
 0010 (2)
00001 (1)


-2 + 1
 1110 (-2)
 0001 (1)
01111 (-1)


 11111111 (-1)
 00000010 (2)
 00000001 (1)
 11111110 (XOR) 
 00000001 (~) USE ~ TO GET NEGATIVE in python

 11111111 (-1)
 11111110 (-2)
 11111101 (-3) (ans in JAVA, but 2**8 - 2 in python)
 00000010 (XOR)
 11111101 (~) USE ~ TO GET NEGATIVE in python
"""


res = getSum(-1, 2)
res2 = getSum2(-1, -5)