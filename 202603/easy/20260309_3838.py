## https://leetcode.com/problems/weighted-word-mapping/

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ""
        for word in words:
            n = 0
            for w in word: n += weights[ord(w)-97]
            ans += chr(122 - n % 26)
        return ans