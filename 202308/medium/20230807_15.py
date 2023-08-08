## https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        lst1, zero, lst3 = [], 0, []
        ans = set()

        for n in nums :
            if n < 0 : lst1.append(n)
            elif n > 0 : lst3.append(n)
            else : zero += 1 # n == 0
        
        s_lst1, s_lst3 = set(lst1), set(lst3)

        ln1 = len(lst1)
        for c1 in range(ln1-1) :
            for c2 in range(c1+1, ln1) :
                num1 = -(lst1[c1] + lst1[c2])
                if num1 in s_lst3 :
                    ans.add(tuple(sorted([lst1[c1], lst1[c2], num1])))

        ln3 = len(lst3)
        for c3 in range(ln3-1) :
            for c4 in range(c3+1, ln3) :
                num3 = -(lst3[c3] + lst3[c4])
                if num3 in s_lst1 :
                    ans.add(tuple(sorted([lst3[c3], lst3[c4], num3])))

        if zero > 0 :
            for num in s_lst1 :
                if -num in s_lst3 :
                    ans.add(tuple([num, 0, -num]))
        if zero >= 3 : ans.add(tuple([0, 0, 0]))
        
        return ans