# https://leetcode.com/problems/design-authentication-manager/


class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.memo = {}
        self.lifetime = timeToLive
        self.n_unexpired = 0

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.memo[tokenId] = currentTime + self.lifetime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.memo:
            return
        expired = self.memo[tokenId]
        if expired <= currentTime: # already expired
            self.memo.pop(tokenId)
        else:
            self.memo[tokenId] = currentTime + self.lifetime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(x>currentTime for x in self.memo.values())


class AuthenticationManager2:

    def __init__(self, timeToLive: int):
        self.memo = {}
        self.lifetime = timeToLive
        self.n_unexpired = 0

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.memo[tokenId] = currentTime + self.lifetime

    def renew(self, tokenId: str, currentTime: int) -> None:

        if tokenId not in self.memo:
            return
        expired = self.memo[tokenId]
        if expired <= currentTime:  # already expired
            self.memo.pop(tokenId)
        else:
            self.memo[tokenId] = currentTime + self.lifetime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        delete = []
        for k, t in self.memo.items():
            if t <= currentTime:
                # delete
                delete.append(k)
            else:
                count += 1
        for i in delete:
            self.memo.pop(i)
        return count

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)