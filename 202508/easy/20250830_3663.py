## https://leetcode.com/problems/find-the-least-frequent-digit/

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        dics, ans = {}, []
        for i in str(n):
            try: dics[i] += 1
            except: dics[i] = 1
        m = min(dics.values())
        for k, v in dics.items():
            if v == m: ans.append(k)
        return int(min(ans))