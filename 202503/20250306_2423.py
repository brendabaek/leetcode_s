## https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        dics1, dics2, = {}, {}
        for w in word :
            try : dics1[w] += 1
            except : dics1[w] = 1
        for d in dics1.values() :
            try : dics2[d] += 1
            except : dics2[d] = 1
        k, v = list(dics2.keys()), list(dics2.values())
        if len(k) == 1 and (k == [1] or v == [1]) : return True
        elif len(k) > 2 : return False
        elif (1, 1) in dics2.items() : return True
        elif max(k) - 1 == min(k) and dics2[max(k)] == 1 : return True
        return False