# https://leetcode.com/problems/verifying-an-alien-dictionary/description/


# first thought, TC:(N^2M) M is length of word in words, SC:O(M)
def isAlienSorted(words: List[str], order: str) -> bool:
    memo = {c: i for i, c in enumerate(order)}  # TC:O(1), SC:O(1)

    # pair check, TC:O(N^2M), M is len of word
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1, word2 = words[i], words[j]
            for c1, c2 in zip(word1, word2):
                if memo[c1] > memo[c2]:
                    return False
                elif memo[c1] < memo[c2]:
                    break
            else:  # loop end
                if len(word1) > len(word2):
                    return False
    return True

# comparison can be transmitted, TC:(NM), M is length of word in words, SC:O(1)
def isAlienSorted2(words: List[str], order: str) -> bool:
    memo = {c: i for i, c in enumerate(order)}  # TC:O(1), SC:O(1)

    # pair check, TC:O(NM), M is len of word, SC:O(1)
    for i in range(len(words) - 1):
        # word1, word2 = words[i], words[i+1]
        for c1, c2 in zip(words[i], words[i + 1]):
            if memo[c1] > memo[c2]:
                return False
            elif memo[c1] < memo[c2]:
                break
        else:  # loop end
            if len(words[i]) > len(words[i + 1]):
                return False
    return True