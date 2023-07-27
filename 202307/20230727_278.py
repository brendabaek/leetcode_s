## https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        mn = 0
        mx = n
        md = n // 2

        if isBadVersion(0) == True : return 0
        while (mx-mn) > 1 :
            if isBadVersion(md) == False : mn = md
            else : mx = md
            md = (mn + mx) // 2
        return mx