## https://leetcode.com/problems/maximum-product-of-three-numbers/

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg, zero, pos = [], 0, []
        for n in nums :
            if n < 0 : neg.append(n)
            elif n > 0 : pos.append(n)
            else : zero += 1
        neg.sort()
        pos.sort()

        if len(neg) == 0 :
            if len(pos) >= 3 :
                return pos[-1] * pos[-2] * pos[-3]
            else : return 0
        
        elif len(neg) == 1 :
            if len(pos) >= 3 :
                return pos[-1] * pos[-2] * pos[-3]
            elif len(pos) == 2 :
                if zero > 0 : return 0
                else : return pos[0] * pos[1] * neg[0]
            else : return 0

        else :
            if len(pos) >= 3 :
                return max((pos[-1] * pos[-2] * pos[-3]), (neg[0] * neg[1] * pos[-1]))
            elif len(pos) == 2 or len(pos) == 1 :
                return neg[0] * neg[1] * pos[-1]
            else :
                if zero > 0 : return 0
                else : return neg[-1] * neg[-2] * neg[-3]
