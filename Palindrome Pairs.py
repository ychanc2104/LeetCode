# https://leetcode.com/problems/palindrome-pairs/
# https://leetcode.com/problems/palindrome-pairs/discuss/2585442/Intuitive-Python3-or-HashMap-or-95-Time-and-Space-or-O(N*W2)


# TC:O(nk^2), SC:O(nk)
def palindromePairs(words):
    # SC:O(nk)
    hashmap = {word: i for i, word in enumerate(words)}
    # print(hashmap)
    n = len(words)
    res = []
    # TC:O(nk^2)
    for i in range(n):  # O(n)
        word = words[i]
        word_reverse = words[i][::-1]
        # case 1, equal length
        if word_reverse in hashmap and i != hashmap[word_reverse]:
            res.append([i, hashmap[word_reverse]])
        # edge case, '' + 'aba'
        if word != '' and word == word_reverse and '' in hashmap:
            res.append([i, hashmap['']])
            res.append([hashmap[''], i])
        # case 2,3 length is not equal, O(k^2)
        for j in range(1, len(word)):  # O(k), from index 1 to exclude word[i] itself
            # lls(i) + s => slls
            # sll[:1] => [hashmap[w], i]
            if word_reverse[:j] in hashmap and word_reverse[j:] == word_reverse[j:][::-1]:  # O(k)
                res.append([hashmap[word_reverse[:j]], i])
            # aasll + saa
            # llsaa[2:] => [i, hashmap[w]]
            if word_reverse[j:] in hashmap and word_reverse[:j] == word_reverse[:j][::-1]:
                res.append([i, hashmap[word_reverse[j:]]])
    return res



# TC:O(nk^2), SC:O(nk)
def palindromePairs2(words):
    memo = {word:i for i, word in enumerate(words)}
    n = len(words) # may contain ''
    res = []
    for i in range(n):
        word = words[i][::-1] # lls => sll
        for j in range(len(word)+1):
            target_word = word[j:] # (sll,''), (ll,s), (l,sl) (s,'')
            center = word[:j]
            # len of words[i] >= words[j]
            if target_word in memo and i!=memo[target_word] and center == center[::-1]:
                res.append([i, memo[target_word]])
            # len of words[i] < words[j]
            if target_word and target_word == target_word[::-1] and center in memo:
                res.append([memo[center], i])
    return res