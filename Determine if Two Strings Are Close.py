# https://leetcode.com/problems/determine-if-two-strings-are-close/description/
# https://leetcode.com/problems/determine-if-two-strings-are-close/solutions/1029064/python-oneliner-with-counter-explained/

import collections

# TC:O(N), SC:O(1)
def closeStrings(word1: str, word2: str) -> bool:
    counter1 = collections.Counter(word1)
    counter2 = collections.Counter(word2)
    # 1.same set of alphabet, 2.same frequency of each alphabet
    return set(word1) == set(word2) and collections.Counter(counter1.values()) == collections.Counter(counter2.values())