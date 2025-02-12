## https://leetcode.com/problems/rings-and-rods/

class Solution:
    def countPoints(self, rings: str) -> int:
        dics, ans = {}, 0
        for i in range(1, len(rings), 2) :
            try : dics[rings[i]].add(rings[i-1])
            except : dics[rings[i]] = set(rings[i-1])
        for v in dics.values() :
            if len(v) == 3 : ans += 1
        return ans