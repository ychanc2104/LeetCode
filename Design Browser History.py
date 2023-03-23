# https://leetcode.com/problems/design-browser-history/


# first thought, TC:O(N) for visit
class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.i = 0

    def visit(self, url: str) -> None:
        self.i += 1
        self.urls = self.urls[:self.i] + [url]


    def back(self, steps: int) -> str:
        self.i = max(self.i-steps, 0)
        return self.urls[self.i]


    def forward(self, steps: int) -> str:
        self.i = min(self.i+steps, len(self.urls)-1)
        return self.urls[self.i]

# two pointers, TC:O(1) for all
class BrowserHistory2:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.i = 0
        self.end = 0

    def visit(self, url: str) -> None:

        self.i += 1
        if self.i == len(self.urls): # exceed array
            self.urls.append(url)
        else:
            self.urls[self.i] = url
        self.end = self.i


    def back(self, steps: int) -> str:
        self.i = max(self.i-steps, 0)
        return self.urls[self.i]


    def forward(self, steps: int) -> str:
        self.i = min(self.i+steps, self.end)
        return self.urls[self.i]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)