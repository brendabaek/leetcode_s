## https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for p in patterns :
            if p in word : ans += 1
        return ans