## https://leetcode.com/problems/happy-number/

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == None : return
        return self.answer(n, [])

    def answer(self, n, loops) :
        if n in loops : return False
        else : loops.append(n)
        sums = 0
        while n > 0 :
            sums += (n % 10) ** 2
            n = n // 10
        if sums == 1 : return True
        else : return self.answer(sums, loops)            