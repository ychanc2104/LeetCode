# https://leetcode.com/problems/lemonade-change/description/

# first thought, TC:O(N), SC:O(1)
def lemonadeChange(bills: List[int]) -> bool:
    counter = {5: 0, 10: 0} # SC:O(1)
    for bill in bills:
        if bill == 5:
            counter[5] += 1
        elif bill == 10:
            if counter[5] == 0:
                return False
            counter[5] -= 1
            counter[10] += 1
        else:  # 5*3 or 10*1+5*1, use 10 first
            if counter[10] > 0 and counter[5] > 0:
                counter[10] -= 1
                counter[5] -= 1
            elif counter[5] >= 3:
                counter[5] -= 3
            else:
                return False
    return True