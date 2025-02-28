## https://leetcode.com/problems/decode-the-message/

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        n, dics, ans = 97, {" ":" "}, ""
        for k in key :
            if k == " " : continue
            if k in dics : continue
            dics[k] = chr(n)
            n += 1
        for m in message : ans += dics[m]
        return ans