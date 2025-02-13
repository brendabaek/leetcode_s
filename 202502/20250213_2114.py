## https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for s in sentences : ans = max(ans, s.count(" "))
        return ans+1