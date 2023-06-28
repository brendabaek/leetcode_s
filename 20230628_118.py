## https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows < 1 : return None
        else :
            ans = []
            preRow = [1]
            for i in range(numRows) :
                newRow = [1]
                for j in range(1, i+1) :
                    if j < i :
                        sums = preRow[j-1] + preRow[j]
                        newRow.append(sums)
                    elif j == i :
                        newRow.append(1)
                        ans.append(preRow)
                        preRow = newRow
            ans.append(newRow)
        return ans