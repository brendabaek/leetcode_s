## https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        v = 'aeiouAEIOU'
        cnt_f, cnt_e = 0, 0
        for i in range(len(s)//2) :
            if s[i] in v : cnt_f += 1
            if s[-i-1] in v : cnt_e += 1
        return cnt_f == cnt_e