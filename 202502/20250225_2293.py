## https://leetcode.com/problems/min-max-game/

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        ln = len(nums)
        while ln > 1 :
            tmp = []
            for i in range(0, ln, 4) :
                tmp.append(min(nums[i], nums[i+1]))
                try : tmp.append(max(nums[i+2], nums[i+3]))
                except : break
            nums, ln = tmp, len(tmp)
        return nums[0]