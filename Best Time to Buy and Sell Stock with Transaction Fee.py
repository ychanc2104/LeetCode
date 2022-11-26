# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solutions/108870/most-consistent-ways-of-dealing-with-the-series-of-stock-problems/


# two states dp, TC:O(N), SC:O(1)
def maxProfit(prices: List[int], fee: int) -> int:
    held = -prices[0]  # max profit held at i
    sold = 0  # max profit sold at i
    for i in range(1, len(prices)):
        price = prices[i]
        sold = max(sold, held + price - fee)  # sell previous stock or wait
        held = max(held, sold - price)  # buy current stock or wait
    return sold