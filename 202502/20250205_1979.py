## https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_num, min_num = max(nums), min(nums)
        for i in range(min_num, 1, -1) :
            if min_num % i == 0 and max_num % i == 0 : return i
        return 1