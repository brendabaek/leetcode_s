## https://leetcode.com/problems/positions-of-large-groups/

class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        ln, stt, cnt, ans = len(s), 0, 1, []
        for i in range(1, ln) :
            if s[i] == s[i-1] : cnt += 1
            else :
                if cnt > 2 : ans.append([stt, i-1])
                stt, cnt = i, 1
            if i == ln-1 and cnt > 2 : ans.append([stt, i])
        return ans