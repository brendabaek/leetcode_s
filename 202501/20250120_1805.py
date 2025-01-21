## https://leetcode.com/problems/number-of-different-integers-in-a-string/

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s, check, l = set(), "", "1234567890"
        for w in word :
            if w in l : check += w
            elif check == "" : pass
            else :
                s.add(int(check))
                check = ""
        if check == "" : return len(s)
        else : s.add(int(check))
        return len(s)