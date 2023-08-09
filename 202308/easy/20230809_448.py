## https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        ln = len(nums)
        ans = []
        pre = 0
        
        for n in nums :
            if n == pre or n == pre+1 : pre = n
            else :
                cnt = 1
                while pre < n-1 :
                    pre += 1
                    ans.append(pre)
                pre = n

        if pre == ln : return ans
        else :
            cnt = 1
            while pre < ln :
                pre += 1
                ans.append(pre)
            return ans