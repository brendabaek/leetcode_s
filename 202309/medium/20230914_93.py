## https://leetcode.com/problems/restore-ip-addresses/

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4 or 12 < len(s) : return []
        return self.make_answer(s, [], [])

    def make_answer(self, s, tmp, ans) :
        if len(tmp) == 4 :
            if s == '' :
                ans.append('.'.join(tmp))
                return ans
            else : return ans
        if len(s) > 0 and s[0] == "0" :
            tmp.append(s[0])
            ans = self.make_answer(s[1:], tmp, ans)
            tmp.pop()
        else :
            for i in range(min(3, len(s))) :
                if int(s[:i+1]) <= 255 :
                    tmp.append(s[:i+1])
                    ans = self.make_answer(s[i+1:], tmp, ans)
                    tmp.pop()
        return ans
            