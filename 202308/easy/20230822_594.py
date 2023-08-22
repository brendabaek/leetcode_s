## https://leetcode.com/problems/longest-harmonious-subsequence/

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        disc = {}
        for n in nums :
            if n in disc : disc[n] += 1
            else : disc[n] = 1
        
        k = sorted(disc.keys())
        ln = len(k)
        ans = 0

        for i in range(ln-1) :
            if k[i]+1 == k[i+1] :
                ans = max(ans, disc[k[i]] + disc[k[i+1]])
        return ans
