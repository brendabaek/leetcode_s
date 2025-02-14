## https://leetcode.com/problems/capitalize-the-title/

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ans = ""
        for i in title.split() :
            if len(i) < 3 : ans = ans + i.lower() + " "
            else : ans = ans + i[0].upper() + i.lower()[1:] + " "
        return ans[:-1]