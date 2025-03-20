## https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        # n, idx, ln, ans = s[0], 1, len(s), 0
        # if n == "0" : z, o = 1, 0
        # else : z, o = 0, 1
        # while idx < ln :
        #     if n == "0" and s[idx] == "0" : z += 1
        #     elif n == "0" and s[idx] == "1" : o = 1
        #     elif n == "1" and s[idx] == "1" : o += 1
        #     else : ans = max(ans, min(z, o)); z = 1
        #     n = s[idx]
        #     idx += 1
        # return ans * 2 if n == "0" else max(ans, min(z, o)) * 2

        # t, ln = "01", len(s)
        # while len(t) <= ln :
        #     if t not in s : return len(t) - 2
        #     else : t = "0" + t + "1"
        # return len(t) - 2

        tmp = '01'
        while tmp in s:
            tmp = '0' + tmp + '1'
        return len(tmp) - 2