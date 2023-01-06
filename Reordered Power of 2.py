# https://leetcode.com/problems/reordered-power-of-2/
# https://leetcode.com/problems/reordered-power-of-2/solutions/149843/c-java-python-straight-forward/


import collections


def reorderedPowerOf2(n: int) -> bool:
    # use counter
    counter = collections.Counter(str(n))
    x = 1
    while x <= 10 ** 9:
        if counter == collections.Counter(str(x)):
            return True
        x <<= 1
    return False