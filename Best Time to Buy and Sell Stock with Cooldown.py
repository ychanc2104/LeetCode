# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solutions/75928/share-my-dp-solution-by-state-machine-thinking/

# space optimized dp + state machine, TC:O(N), SC:O(1)
def maxProfit(prices: List[int]) -> int:
    sold = float("-inf")  # no way to sell (max profit end with sold)
    held = -prices[0]  # buy first (max profit end with held)
    reset = 0  # (max profit end with reset)
    for i in range(1, len(prices)):
        price = prices[i]
        presold = sold
        sold = held + price  # previous held + sell current, must go forward
        held = max(held, reset - price)  # must go from reset or stay
        reset = max(reset, presold)  # must go from previous sold or stay
    return max(sold, reset)  # held at the end must not be answer