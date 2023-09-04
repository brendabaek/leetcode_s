## https://leetcode.com/problems/combinations/

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.make_answer(1, n, k, [], [])[1]
        
    def make_answer(self, stt, n, k, tmp, ans) :
        if k == 0 :
            ans.append(tmp)
            tmp = tmp[:-1]
            return tmp, ans
        else :
            for i in range(stt, n-k+2) :
                tmp.append(i)
                tmp, ans = self.make_answer(i+1, n, k-1, tmp, ans)
            try : tmp.pop()
            except : pass
            return tmp, ans