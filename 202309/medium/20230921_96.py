## https://leetcode.com/problems/unique-binary-search-trees/

dics = {0:1}
for num in range(1, 20) :
    ans = 0
    for i in range(1, num+1) :
        left, right = i-1, num-i
        ans += dics[left] * dics[right]
    dics[num] = ans

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """            
        return dics[n]