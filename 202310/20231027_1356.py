## https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dics, ans = {}, []
        for a in arr :
            try : dics[bin(a).count('1')] += [a]
            except : dics[bin(a).count('1')] = [a]
        for num in sorted(dics) :
            dics[num].sort()
            ans += dics[num]
        return ans