# https://leetcode.com/problems/encode-and-decode-tinyurl/
# https://leetcode.com/problems/encode-and-decode-tinyurl/solutions/100268/two-solutions-and-thoughts/
# https://leetcode.com/problems/encode-and-decode-tinyurl/solutions/1110529/python-use-two-dictionaries-explained/

import random

class Codec:

    def __init__(self):
        self.l_to_s = {}
        self.s_to_l = {}
        self.code = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        while longUrl not in self.l_to_s:
            short = ''.join(random.choice(self.code) for _ in range(6))
            while short in self.s_to_l:
                short = ''.join(random.choice(self.code) for _ in range(6))
            self.l_to_s[longUrl] = short
            self.s_to_l[short] = longUrl
        return 'http://tinyurl.com/' + short

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.s_to_l[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
