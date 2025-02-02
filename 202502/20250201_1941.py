## https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dics = {}
        for i in s :
            try : dics[i] += 1
            except : dics[i] = 1
        return True if len(set(dics.values())) == 1 else False