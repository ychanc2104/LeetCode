# https://leetcode.com/problems/encode-and-decode-strings/
# https://leetcode.com/problems/encode-and-decode-strings/discuss/70448/1%2B7-lines-Python-(length-prefixes)

# first thought, use ord(), chr()
class Codec:
    def encode(self, strs) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        for word in strs:
            res += [','.join([str(ord(e)) for e in word])] if word else ['$']
        return '#'.join(res)

    def decode(self, s: str):
        """Decodes a single string to a list of strings.
        """
        res = s.split('#')
        ans = []
        for word in res:
            if word == '$':
                decode_word = ""
            else:
                decode_word = ''.join([chr(int(encode_s)) for encode_s in word.split(',')])
            ans += [decode_word]
        return ans


# use chr() convert length to ASCII and connect with original word, TC:O(N), SC:O(1)
class Codec2:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ''
        for word in strs:
            res  += chr(len(word)) + word # length between [0,200]
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        #print(s)
        pos = 0
        res = []
        while pos < len(s):
            length = int(ord(s[pos:pos+1])) # 3 digit
            word = s[pos+1 : pos+1+length]
            #print(length, word)
            res.append(word)
            pos += length+1
        return res

# store digit and string length into encode string
class Codec3:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # store length into encode string
        res = []
        for s in strs:
            l = len(s)
            if 0 <= l <= 9:
                digit = 1
            elif l <= 99:
                digit = 2
            else:
                digit = 3
            res.extend([str(digit), str(l), s])
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        n = len(s)
        L = 0
        while L < n:
            digit = int(s[L])
            l = int(s[L + 1:L + digit + 1])
            L += digit
            res.append(s[L + 1: L + l + 1])
            L += l + 1
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))