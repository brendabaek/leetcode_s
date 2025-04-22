## https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

class Solution:
    def findLatestTime(self, s: str) -> str:
        ans = ""
        if s[0] == "0" and s[1] == "?": ans += "09:"
        elif s[0] == "1" and s[1] == "?": ans += "11:"
        elif s[0] == "?" and s[1] == "?": ans += "11:"
        elif s[0] == "?" and s[1] in ["0", "1"]: ans += "1" + s[1] + ":"
        elif s[0] == "?": ans += "0" + s[1] + ":"
        else: ans += s[:3]
        if s[3] == "?": ans += "5"
        else: ans += s[3]
        if s[4] == "?": ans += "9"
        else: ans += s[4]
        return ans

        # s = list(s)
        # if s[0] == "0" and s[1] == "?": s[1] = "9"
        # elif s[0] == "1" and s[1] == "?": s[1] = "1"
        # elif s[0] == "?" and s[1] == "?": s[0] = "1"; s[1] = "1"
        # elif s[0] == "?" and s[1] in ["0", "1"]: s[0] = "1"
        # elif s[0] == "?": s[0] = "0"
        # if s[3] == "?": s[3] = "5"
        # if s[4] == "?": s[4] = "9"
        # return "".join(s)