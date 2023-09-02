## https://leetcode.com/problems/edit-distance/

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ln1, ln2 = len(word1), len(word2)
        ans = [ [0 for _ in range(ln2+1)] for _ in range(ln1+1) ]
        for i in range(1, ln1+1) : ans[i][0] = i
        for j in range(1, ln2+1) : ans[0][j] = j
        for i in range(1, ln1+1) :
            for j in range(1, ln2+1) :
                if word1[i-1] == word2[j-1] :
                    ans[i][j] = ans[i-1][j-1]
                else :
                    ans[i][j] = min(ans[i-1][j-1], ans[i][j-1], ans[i-1][j])+1
        return ans[ln1][ln2]