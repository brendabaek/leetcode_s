## https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ln = len(height)
        ans = 0
        for i in range(ln-1) :
            if height[i] == 0 : continue
            num = i + (ans//height[i])
            cnt = num - i
            for j in range(num+1, ln) :
                cnt += 1
                ans = max(ans, (min(height[i], height[j]) * cnt))
        return ans