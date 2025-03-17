## https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        s, ans, idx = 0, [], len(nums)-1
        for num in nums :
            ans.append(s); s += num
        s = 0
        for num in nums[::-1] :
            ans[idx] = abs(ans[idx] - s)
            s += num; idx -= 1
        return ans