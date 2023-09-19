## https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd, even, ans = [], [], []
        for num in nums :
            if num % 2 == 1 : odd.append(num)
            else : even.append(num)
        for i in range(len(odd)) : ans += [even[i], odd[i]]
        return ans