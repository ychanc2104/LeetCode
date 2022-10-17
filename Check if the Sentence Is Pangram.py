# https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/




def checkIfPangram(sentence: str) -> bool:
    return len(set(sentence)) == 26