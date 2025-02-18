## https://leetcode.com/problems/counting-words-with-a-given-prefix/

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ln, ans = len(pref), 0
        for word in words :
            if word[:ln] == pref : ans += 1
        return ans