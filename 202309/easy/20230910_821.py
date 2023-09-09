## https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        ln, idx, ans, ans1, ans2 = len(s), s.index(c), [], [], []
        for i in range(ln) :
            if s[i] != c : ans1.append(abs(idx-i))
            else :
                ans1.append(0)
                if i != idx : idx = i
                
        s = s[::-1]
        idx = s.index(c)
        for i in range(ln) :
            if s[i] != c : ans2.append(abs(idx-i))
            else :
                ans2.append(0)
                if i != idx : idx = i

        for i in range(ln) :
            m = min(ans1[i], ans2[ln-i-1])
            ans.append(m)
        return ans