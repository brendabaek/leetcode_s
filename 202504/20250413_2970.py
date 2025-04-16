## https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        ln, ans = len(nums), 0
        for i in range(ln):
            lst1 = nums[:i]
            check1 = True
            for idx1 in range(1, len(lst1)):
                if lst1[idx1-1] >= lst1[idx1]: check1 = False; break
            if check1 == False: break
            for j in range(i+1, ln+1):
                lst2 = nums[j:]
                if lst1 == [] or lst2 == [] : pass
                elif lst1[-1] >= lst2[0] : continue
                check2 = True
                for idx2 in range(1, len(lst2)) :
                    if lst2[idx2-1] >= lst2[idx2] : check2 = False; break
                if check2 == True : ans += ln - j + 1; break
        return ans