## https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ln = len(s)
        lst = [ln-2-i for i in range(ln)]
        for i in range(ln) :
            stt = s[i]
            for j in range(ln-1, i, -1) :
                if stt == s[j] : break
                else : lst[i] -= 1
        return max(lst)