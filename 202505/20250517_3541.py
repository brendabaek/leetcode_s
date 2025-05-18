## https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

class Solution:
    def maxFreqSum(self, s: str) -> int:
        dics1, dics2 = {"a": 0}, {"b": 0}
        for i in s:
            if i in "aeiou":
                try: dics1[i] += 1
                except: dics1[i] = 1
            else:
                try: dics2[i] += 1
                except: dics2[i] = 1
        return max(dics1.values()) + max(dics2.values())