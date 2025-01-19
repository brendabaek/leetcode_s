## https://leetcode.com/problems/second-largest-digit-in-a-string/

class Solution:
    def secondHighest(self, s: str) -> int:
        n = "1234567890"
        l = set()
        for i in s :
            if i in n : l.add(int(i))
        l = list(l)
        l.sort()
        return l[-2] if len(l) >= 2 else -1