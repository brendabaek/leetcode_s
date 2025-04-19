## https://leetcode.com/problems/split-the-array/

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums.sort()
        p, cnt = 0, 0
        for num in nums:
            if num == p: cnt +=1
            else: p = num; cnt = 1
            if cnt > 2: return False
        return True