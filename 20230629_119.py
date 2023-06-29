## https://leetcode.com/problems/pascals-triangle-ii/

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1]
        for i in range(1, rowIndex+1) :
            now = [1]
            for j in range(1, i+1) :
                if j == i : now.append(1)
                else : now.append(ans[j-1] + ans[j])
            ans = now
        return ans