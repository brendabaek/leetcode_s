## https://leetcode.com/problems/find-the-distinct-difference-array/

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        idx, ln, s1, ans = 0, len(nums), set(), []
        while idx < ln :
            s1.add(nums[idx])
            s2 = set(nums[idx+1:])
            ans.append(len(s1) - len(s2))
            idx += 1
        return ans