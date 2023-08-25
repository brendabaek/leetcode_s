## https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = nums[0]
        max_sum = current_sum
        for i in range(1, len(nums)) :
            print(nums[i], current_sum, max_sum)
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum

        lst, tmp = [], nums[0]
        for i in range(len(nums)-1) :
            if nums[i] * nums[i+1] > 0 : tmp += nums[i+1]
            else :
                lst.append(tmp)
                tmp = nums[i+1]
        lst.append(tmp)
        ans = max(max(nums), max(lst))
        if len(lst) == 1 : return ans

        pre, sums = max(lst[0], lst[1]), 0
        for i in range(len(lst)) :
            if lst[i] < sums : pass
            else :
                sums = lst[i]
                for j in range(i+1, len(lst)) :
                    sums += lst[j]
                    if sums < 0 : break
                    else : ans = max(ans, sums)
        return ans