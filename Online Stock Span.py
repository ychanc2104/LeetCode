# https://leetcode.com/problems/online-stock-span/description/


# monotonic stack, TC: amortized O(1), SC:O(N)
class StockSpanner:

    def __init__(self):
        self.stack = []  # store price and res, monotically decreasing

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            p2, res2 = self.stack.pop()
            res += res2
        self.stack.append((price, res))
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)