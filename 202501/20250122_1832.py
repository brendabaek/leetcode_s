## https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set()
        for i in sentence : s.add(i)
        return True if len(s) == 26 else False