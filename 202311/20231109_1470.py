## https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lst, ans = nums[n:], []
        for i in range(n) :
            ans.append(nums.pop(0))
            ans.append(lst.pop(0))
        return ans