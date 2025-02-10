## https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        dics1, dics2 = {}, {}
        for w1 in word1 :
            try : dics1[w1] += 1
            except : dics1[w1] = 1
        for w2 in word2 :
            try : dics2[w2] += 1
            except : dics2[w2] = 1
        for k, v in dics1.items() :
            if k not in dics2 :
                if v > 3 : return False
            else :
                if abs(v - dics2[k]) > 3 : return False
                else : del dics2[k]
        for v in dics2.values() :
            if v > 3 : return False
        return True