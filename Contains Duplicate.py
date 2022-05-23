# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums) -> bool:
    return not len(set(nums)) == len(nums)


def containsDuplicate2(nums) -> bool:
    return len(nums)>len(set(nums))
