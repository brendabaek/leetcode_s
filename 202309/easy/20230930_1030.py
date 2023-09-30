## https://leetcode.com/problems/matrix-cells-in-distance-order/

class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        max_rows = max(abs(rows-rCenter), rCenter)
        max_cols = max(abs(cols-cCenter), cCenter)
        ans = []
        for m in range(max_rows+max_cols+1) :
            for i in range(m+1) :
                j = m-i
                if i != 0 and j != 0 and \
                    rCenter-i >= 0 and cCenter-j >= 0 and rCenter-i < rows and cCenter-j < cols :
                    ans.append([rCenter-i, cCenter-j])
                if i != 0 and rCenter-i >= 0 and cCenter+j >= 0 and rCenter-i < rows and cCenter+j < cols :
                    ans.append([rCenter-i, cCenter+j])
                if j != 0 and rCenter+i >= 0 and cCenter-j >= 0 and rCenter+i < rows and cCenter-j < cols :
                    ans.append([rCenter+i, cCenter-j])
                if rCenter+i >= 0 and cCenter+j >= 0 and rCenter+i < rows and cCenter+j < cols :
                    ans.append([rCenter+i, cCenter+j])
        return ans