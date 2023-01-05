# https://leetcode.com/problems/filling-bookcase-shelves/description/
# https://leetcode.com/problems/filling-bookcase-shelves/solutions/374938/dfs-explanation-try-adding-a-book-to-the-current-shelf-and-next-one/
# https://leetcode.com/problems/filling-bookcase-shelves/solutions/323305/dfs-memo/

from functools import lru_cache


# top-down dp, TC:O(), SC:O()
def minHeightShelves(books: List[List[int]], shelfWidth: int) -> int:
    # partition books with adjacent or new shelf
    @lru_cache(None)
    def helper(i, shelfHeight, remainingWidth): # min height of books[i:]
        if remainingWidth < 0:
            return float("inf")
        if i == len(books):
            return shelfHeight
        w, h = books[i]
        adj = helper(i + 1, max(shelfHeight, h), remainingWidth - w)
        # previous shelf height of books[:i+1] + min height of books[i+1:]
        new = shelfHeight + helper(i + 1, h, shelfWidth - w)  # place i book to new shelve
        return min(adj, new)

    return helper(0, 0, shelfWidth)

# top-down dp, TC:O(), SC:O()
def minHeightShelves2(books: List[List[int]], shelfWidth: int) -> int:
        dp = {} # min height of books[i:]
        def helper(i, shelfHeight, remainingWidth):
            if remainingWidth < 0:
                return float("inf")
            if (i, shelfHeight, remainingWidth) in dp:
                return dp[(i, shelfHeight, remainingWidth)]
            if i == len(books):
                return shelfHeight
            w, h = books[i]
            adj = helper(i+1, max(shelfHeight, h), remainingWidth - w)
            new = shelfHeight + helper(i+1, h, shelfWidth - w) # place i book to new shelve
            dp[(i, shelfHeight, remainingWidth)] = min(adj, new)
            return dp[(i, shelfHeight, remainingWidth)]

        return helper(0, 0, shelfWidth)


# bottom-up dp, TC:O(N^2), SC:O(N)
def minHeightShelves3(books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1) # min height of books[i:]
        for i in range(1, n+1):
            width, height = books[i-1]
            dp[i] = height + dp[i-1] # initiate with new shelf
            for j in range(i - 2, -1, -1):  # try partition, move i-2 to be adjacent first until exceed shelfWidth
                if width + books[j][0] > shelfWidth:
                    break
                width += books[j][0] # try adjacent with j and old shlef 0~j-1
                height = max(height, books[j][1]) # update max height in the previous shlef
                dp[i] = min(dp[i], height + dp[j]) # compare with current book height + previous shelf
        return dp[-1]