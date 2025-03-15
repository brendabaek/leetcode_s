## https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ans = 0
        for num in nums :
            ans += num
            while num > 0 :
                ans -= num % 10
                num = num // 10
            # num = str(num)
            # for n in num : d_sum += int(n)
        return abs(ans)