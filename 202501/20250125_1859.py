## https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        lst = sorted((w[-1], w[:-1]) for w in s.split())
        return " ".join(l[1] for l in lst)