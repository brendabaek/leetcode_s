## https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

class Solution:
    def digitCount(self, num: str) -> bool:
        ln = len(num)
        dics = {str(i):0 for i in range(ln)}
        for n in num :
            try : dics[n] += 1
            except : return False
        for i in range(ln) :
            if dics[str(i)] != int(num[i]) : return False
        return True