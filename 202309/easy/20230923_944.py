## https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        cnt, ln, ln_s = 0, len(strs), len(strs[0])
        for i in range(ln_s) :
            tmp =  ord(strs[0][i])
            for j in range(1, ln) :
                if tmp <= ord(strs[j][i]) : tmp = ord(strs[j][i])
                else :
                    cnt += 1
                    break
        return cnt