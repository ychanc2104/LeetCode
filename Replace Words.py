# https://leetcode.com/problems/replace-words/description/?envType=daily-question&envId=2024-06-07


# TC:O(NlogN + NMk), k:average length word in dictionary, SC:O(N) for sorting
def replaceWords(dictionary: List[str], sentence: str) -> str:
    res = []
    dictionary.sort()
    for word in sentence.split(" "):
        for d in dictionary:
            if word.startswith(d):
                word = d
                break
        res.append(word)

    return ' '.join(res)

# TC:O(Nk + Mk^2), k:average length word in dictionary, SC:O(Nk)
def replaceWords2(dictionary: List[str], sentence: str) -> str:
    res = []
    d = set(dictionary)

    for word in sentence.split(" "): # M
        for i in range(len(word)):
            s = word[:i+1]
            if s in d:
                word = s
                break
        res.append(word)

    return ' '.join(res)


# TC:O(Nk + Mk), k:average length word in dictionary, SC:O(Nk)
def replaceWords3(dictionary: List[str], sentence: str) -> str:
    trie = {}
    for d in dictionary: # N
        node = trie
        for c in d:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = d

        res = []
        for word in sentence.split(" "):
            # search word in trie
            node = trie
            add_word = word
            for c in word:
                if c not in node:
                    break
                node = node[c]
                if '#' in node:
                    add_word = node['#']
                    break
            res.append(add_word)

    return ' '.join(res)
