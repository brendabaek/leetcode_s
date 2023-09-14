## https://leetcode.com/problems/lemonade-change/

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        cnt5, cnt10 = 0, 0
        for b in bills :
            if b == 5 : cnt5 += 1
            elif b == 10 :
                if cnt5 == 0 : return False
                else :
                    cnt10 += 1
                    cnt5 -= 1
            elif b == 20 :
                if cnt10 >= 1 and cnt5 >= 1 :
                    cnt10 -= 1
                    cnt5 -= 1
                elif cnt5 >= 3 : cnt5 -= 3
                else : return False
        return True