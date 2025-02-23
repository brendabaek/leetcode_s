## https://leetcode.com/problems/count-prefixes-of-a-given-string/

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for word in words :
            if word == s[:len(word)] : ans += 1
        return ans