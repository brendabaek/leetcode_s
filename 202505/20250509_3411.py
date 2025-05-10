## https://leetcode.com/problems/maximum-subarray-with-equal-products/

class Solution:
    def prod(self, nums):
        result = 1
        for num in nums: result *= num
        return result
    def gcd(self, a, b):
        while b: a, b = b, a % b
        return a
    def lcm(self, a, b): return a * b // gcd(a, b)
    def gcd_list(self, nums):
        result = nums[0]
        for num in nums[1:]: result = gcd(result, num)
        return result
    def lcm_list(self, nums):
        result = nums[0]
        for num in nums[1:]: result = lcm(result, num)
        return result
        
    def maxLength(self, nums: List[int]) -> int:
        ln = len(nums)
        for j in range(ln, 0, -1):
            for i in range(ln - j + 1):
                if self.prod(nums[i:i+j]) == self.lcm_list(nums[i:i+j]) * self.gcd_list(nums[i:i+j]): return j