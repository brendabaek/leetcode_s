## https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num = max(nums)
        nums.remove(num)
        return (num-1)*(max(nums)-1)