## https://leetcode.com/problems/number-of-beautiful-pairs/

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans, ln = 0, len(nums)
        for i in range(ln-1) :
            s = nums[i]
            while s >= 10 : s //= 10
            for j in range(i+1, ln) :
                if gcd(s, nums[j] % 10) == 1 : ans += 1                
        return ans