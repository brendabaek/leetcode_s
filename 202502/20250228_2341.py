## https://leetcode.com/problems/maximum-number-of-pairs-in-array/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ans = [0, 0]
        while nums != [] :
            target = nums.pop()
            try :
                nums.remove(target)
                ans[0] += 1
            except : ans[1] += 1
        return ans