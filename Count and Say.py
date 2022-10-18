# https://leetcode.com/problems/count-and-say/description/


# first thought
def countAndSay(n: int) -> str:
    if n == 1:
        return '1'

    def say(s):
        if len(s) == 1:
            return '1' + s
        count = 1
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                return str(count) + s[i - 1] + say(s[i:])
            count += 1
        return str(count) + s[i]

    return say(countAndSay(n - 1))


# refine, recursive, TC:O(), SC:O()
def countAndSay2(n: int) -> str:
    if n == 1:
        return '1'
    def say(s, pos=0, count=1):
        if pos == len(s)-1:
            return f"{count}{s[pos]}"
        if s[pos] != s[pos+1]:
            return f"{count}{s[pos]}{say(s, pos+1, 1)}"
        return say(s, pos+1, count+1)
    return say(countAndSay2(n-1))