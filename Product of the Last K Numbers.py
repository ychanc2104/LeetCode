# https://leetcode.com/problems/product-of-the-last-k-numbers/description/
# https://leetcode.com/problems/product-of-the-last-k-numbers/solutions/510260/java-c-python-prefix-product/



class ProductOfNumbers:

    def __init__(self):
        # self.data = []
        self.prefix = [1] # prefix[i]: product of data[0:i+1], if encounter append 1
    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # nums:     2,2,3,4
        # prefix: 1,2,4,12,48
        # nums:     2,0,3,4
        # prefix:     1,3,12
        n = len(self.prefix)
        return self.prefix[-1]//self.prefix[-1-k] if k<n else 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)