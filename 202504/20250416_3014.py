## https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

class Solution:
    def minimumPushes(self, word: str) -> int:
        ln, ans = len(word), 0
        for i in range(1, (ln//8)+1): ans += i * 8
        return ans + ((ln // 8) + 1) * (ln % 8)