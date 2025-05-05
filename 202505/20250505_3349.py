## https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-k-k+1):
            check = True
            for j in range(k-1):
                if nums[i+j] >= nums[i+j+1]: check = False
            if check == False: continue
            for l in range(k-1):
                if nums[i+k+l] >= nums[i+k+l+1]: check = False
            if check == True: return True
        return False

        # if k == 1: return True
        # p, check = nums[0], [True]
        # for num in nums[1:]:
        #     if num > p: check.append(True)
        #     else: check.append(False)
        #     p = num
        # for i in range(len(nums)-k-k+1):
        #     if set(check[i:i+k][1:]) == {True} and set(check[i+k:i+k+k][1:]) == {True}: return True
        # return False