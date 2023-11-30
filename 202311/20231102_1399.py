## https://leetcode.com/problems/count-largest-group/

class Solution:
    def countLargestGroup(self, n: int) -> int:
        ans, dics = 0, {}
        for i in range(1, n+1) :
            sums = 0
            for n in str(i) : sums += int(n)
            try : dics[sums] += 1
            except : dics[sums] = 1
        m = max(dics.values())
        for v in dics.values() :
            if m == v : ans += 1
        return ans