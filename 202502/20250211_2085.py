## https://leetcode.com/problems/count-common-words-with-one-occurrence/

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dics1, dics2, ans = {}, {}, 0
        for w1 in words1 :
            try : dics1[w1] += 1
            except : dics1[w1] = 1
        for w2 in words2 :
            try : dics2[w2] += 1
            except : dics2[w2] = 1
        for k, v in dics1.items() :
            if k not in dics2 or v > 1 : continue
            if dics2[k] == 1 : ans += 1
        return ans