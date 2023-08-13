## https://leetcode.com/problems/next-permutation/

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        ln, p = len(nums), -1
        if ln <= 2 : return nums.append(nums.pop(0))
        for i in range(ln-2, -1, -1) :
            if nums[i+1] > nums[i] :
                for j in range(ln-1, i, -1) :
                    if nums[j] > nums[i] :
                        nums.insert(i, nums.pop(j))
                        break
                cnt, p = i+1, i
                while cnt < ln-1 :
                    nums.insert(cnt, nums.pop(cnt+nums[cnt:].index(min(nums[cnt:]))))
                    cnt += 1
                break
        if p == -1 : nums.sort()