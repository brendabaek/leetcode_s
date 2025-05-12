## https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

class Solution:
    def maxDifference(self, s: str) -> int:
        o, e = 0, 100
        for i in set(s):
            if s.count(i) % 2 == 1 and s.count(i) > o: o =s.count(i)
            elif s.count(i) % 2 == 0 and s.count(i) < e: e = s.count(i)
        return o - e