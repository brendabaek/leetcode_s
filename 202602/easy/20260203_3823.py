## https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/

class Solution:
    def reverseByType(self, s: str) -> str:
        l1, l2 = [], []
        for l in s:
            if l.isalpha(): l1.append(l)
            else: l2.append(l)
        ans = ""
        for l in s:
            if l.isalpha(): ans += l1.pop()
            else: ans += l2.pop()
        return ans