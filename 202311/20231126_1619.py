## https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        ln = len(arr)
        idx = ln // 20
        return sum(arr[idx:-idx]) / (ln-(idx*2))