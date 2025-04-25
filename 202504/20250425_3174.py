## https://leetcode.com/problems/clear-digits/

class Solution:
    def clearDigits(self, s: str) -> str:
        n, lst = "0123456789", []
        for l in s:
            try:
                if l in n and lst[-1] not in n: lst.pop()
                else: lst.append(l)
            except: lst.append(l)
        return "".join(lst)