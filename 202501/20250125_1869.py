## https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        dics = {'0':0, '1':0}
        n, c = s[0], 1
        for i in s[1:] :
            if i == n : c += 1
            else :
                dics[n] = max(dics[n], c)
                n, c = i, 1
        dics[n] = max(dics[n], c)
        return True if dics['1'] > dics['0'] else False