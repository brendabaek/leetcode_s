## https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        return self.make_answer(s)

    def make_answer(self, s) :
        idx = 1
        while idx < len(s) :
            if s[idx-1] == s[idx] :
                s = s[:idx-1]+s[idx+1:]
                # idx = max(idx-1, 1)
                if idx > 1 : idx -= 1
            else : idx += 1
        return s