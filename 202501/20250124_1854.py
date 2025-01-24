## https://leetcode.com/problems/maximum-population-year/

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        arr = [0] * 101
        for log in logs :
            for i in range(log[0], log[1]) : arr[i-1950] += 1
        return arr.index(max(arr)) + 1950