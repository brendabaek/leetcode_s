## https://leetcode.com/problems/number-of-equivalent-domino-pairs/

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        while len(dominoes) > 0 :
            doms = dominoes[0]
            cnt1 = dominoes.count(doms)-1
            if doms[0] == doms[1] : cnt2 = 0
            else : cnt2 = dominoes.count(doms[::-1])
            for j in range(cnt1+cnt2+1) : ans += j
            dominoes = [d for d in dominoes if d != doms]
            dominoes = [d for d in dominoes if d != doms[::-1]]
        return ans