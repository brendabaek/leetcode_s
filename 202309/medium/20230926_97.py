## https://leetcode.com/problems/interleaving-string/

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3) : return False
        dp = [[-1] * (len(s2)+1) for _ in range(len(s1)+1)]
        return self.make_answer(s1, s2, s3, 0, 0, dp)

    def make_answer(self, s1, s2, s3, idx1, idx2, dp) :
        if idx1 + idx2 == len(s3) : return True
        if dp[idx1][idx2] != -1 : return dp[idx1][idx2] == 1
        ans = False

        if idx1 < len(s1) and s1[idx1] == s3[idx1+idx2] :
            ans |= self.make_answer(s1, s2, s3, idx1+1, idx2, dp)
        if idx2 < len(s2) and s2[idx2] == s3[idx1+idx2] :
            ans |= self.make_answer(s1, s2, s3, idx1, idx2+1, dp)
        if ans == True : dp[idx1][idx2] = 1
        else : dp[idx1][idx2] = 0
        return ans