## https://leetcode.com/problems/find-lucky-integer-in-an-array/

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort(reverse=True)
        pre, cnt = None, 0
        for a in arr :
            if pre == a : cnt += 1
            else :
                if pre == cnt : return cnt
                else : cnt, pre = 1, a
        return cnt if pre == cnt else -1