## https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ln, dics, ans = len(s), {}, ""
        for i in range(ln) : dics[indices[i]] = s[i]
        for j in range(ln) : ans += dics[j]
        return ans