# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/solutions/834376/very-simple-python-solution-with-follow-up/

class SparseVector:
    # TC:O(N), SC:O(N)
    def __init__(self, nums: List[int]):
        self.memo = {i:num for i,num in enumerate(nums) if num != 0}

    # TC:O(N)
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i,num in vec.memo.items():
            res += self.memo.get(i, 0) * num
        return res



# follow-up, only one sparse vector
class SparseVector2:
    def __init__(self, nums: List[int]):
        self.memo = {i:num for i,num in enumerate(nums) if num != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        # follow-up, one sparse only, check which with less key
        res = 0
        sparse_dict = self.memo
        another_dict = vec.memo
        if len(self.memo) > len(vec.memo): # exchange
            sparse_dict, another_dict = another_dict, sparse_dict

        for i,num in sparse_dict.items():
            res += another_dict.get(i, 0) * num
        return res



# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)