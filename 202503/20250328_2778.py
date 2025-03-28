## https://leetcode.com/problems/sum-of-squares-of-special-elements/

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ln, ans = len(nums), 0
        # for i in range(ln) :
        #     if ln % (i+1) == 0 : ans += nums[i] ** 2
        # return ans
        
        for i in range(1, int(ln ** 0.5) + 1) :
            if ln % i == 0 : ans += nums[i-1] ** 2 + nums[(ln//i)-1] ** 2
        if i ** 2 == ln : ans -= nums[(ln//i)-1] ** 2
        return ans