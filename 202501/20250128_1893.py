## https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        for r in ranges :
            if r[1] < left : continue
            if left < r[0] : return False
            if right <= r[1] : return True
            left = r[1] + 1
        return False