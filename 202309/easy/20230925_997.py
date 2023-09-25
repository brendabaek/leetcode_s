## https://leetcode.com/problems/find-the-town-judge/

class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if trust == [] and n == 1 : return 1
        num, cnt, ans = {}, {}, False
        for t in trust :
            try : num[t[0]] += [t[1]]
            except : num[t[0]] = [t[1]]
            try : cnt[t[1]] += 1
            except : cnt[t[1]] = 1
        for k, v in cnt.items() :
            if v == n-1 :
                if k not in num : return k
                for n in num[k] :
                    if n in num :
                        ans = False
                        break
                    else : ans = True
                if ans == True : return k
        return -1

