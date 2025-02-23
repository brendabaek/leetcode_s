## https://leetcode.com/problems/find-closest-number-to-zero/

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = 100001
        for num in nums :
            if num == 0 : return 0
            if abs(num) < abs(ans) : ans = num
            elif num + ans == 0 : ans = abs(ans)
        return ans