# https://leetcode.com/problems/minimum-window-substring/
# https://leetcode.com/problems/minimum-window-substring/discuss/226911/Python-two-pointer-sliding-window-with-explanation

from collections import Counter

def check_valid(s, t):
    t_map = {c:0 for c in t}

    for c in t:
        if s.find(c, t_map[c])==-1:
            return False
        else:
            t_map[c] = s.find(c, t_map[c])+1
    return True




def minWindow(s, t):
    L, R = 0, 0
    res = s
    # for i in range(len(s)+len(t)):
    while R<=len(s):
        print(s[L:R], L, R)
        if check_valid(s[L:R], t):
            while check_valid(s[L:R], t):
                if len(s[L:R])<len(res):
                    res = s[L:R]
                L += 1
        else:
            R += 1
    return res




def minWindow2(s, t):
    from collections import Counter
    L, R = 0, 0
    t_counter = Counter(t)
    res_counter = Counter()
    res = ''
    for c in s:
        # in t
        if t_counter[c] > 0:
            res_counter[c] += 1
        R += 1
        # valid
        valid = res_counter & t_counter
        # if sum(valid.values()) >= len(t):
        while sum(valid.values()) == len(t):
            res = s[L:R] if len(s[L:R]) < len(res) or res == '' else res
            if t_counter[s[L]] > 0:
                res_counter[s[L]] -= 1
            L += 1
            valid = res_counter & t_counter
    return res

def minWindow3(search_string, target):
    from collections import Counter
    target_letter_counts = Counter(target)
    start = 0
    end = 0
    min_window = ""
    target_len = len(target)
    for end in range(len(search_string)):
        # If we see a target letter, decrease the total target letter count
        if target_letter_counts[search_string[end]] > 0:
            target_len -= 1

        target_letter_counts[search_string[end]] -= 1
        print(target_letter_counts, target_len)
        # If all letters in the target are found:
        while (target_len == 0):
            window_len = end - start + 1
            if not min_window or window_len < len(min_window):
                # Note the new minimum window
                min_window = search_string[start: end + 1]

            # Increase the letter count of the current letter
            target_letter_counts[search_string[start]] += 1

            # If all target letters have been seen and now, a target letter is seen with count > 0
            # Increase the target length to be found. This will break out of the loop
            if target_letter_counts[search_string[start]] > 0:
                target_len += 1
            start += 1
    return min_window

def minWindow3(search_string, target):

    from collections import Counter

    L, R = 0, 0
    t_counter = Counter(t)
    l = len(t)
    res = ''
    for c in s:
        if t_counter[c] > 0:
            l -= 1
        t_counter[c] -= 1
        R += 1

        while l == 0:
            res = s[L:R] if R - L < len(res) or not res else res
            t_counter[s[L]] += 1
            if t_counter[s[L]] > 0:
                l += 1
            L += 1
    return res



s = "cabefgecdaecf"
t = "caec"


res = minWindow(s, t)


res2 = minWindow2(s,t)

res3 = minWindow3(s,t)