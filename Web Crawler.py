# https://leetcode.com/problems/web-crawler/description/



# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
class HtmlParser(object):
   def getUrls(self, url):
       """
       :type url: str
       :rtype List[str]
       """

# first thought, dfs, TC:O(Mk), M is number of edges, k is len of url, SC:O(Nk), N is number of url list
def crawl(startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
    hostname = startUrl.split('/')[2]
    res = []
    visited = set()
    def helper(url):
        if url in visited or url.split('/')[2] != hostname: return
        visited.add(url)
        res.append(url)
        for nei in htmlParser.getUrls(url):
            helper(nei)
    helper(startUrl)
    return res