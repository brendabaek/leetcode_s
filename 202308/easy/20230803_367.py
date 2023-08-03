## https://leetcode.com/problems/valid-perfect-square/

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 10 :
            for i in range(4) :
                if num == i * i : return True
            return False
        
        nums = num
        cnt = 0

        while nums // 10 > 0 :
            nums = nums // 10
            cnt += 1
            
        if cnt % 2 == 0 : stt, end = 10 ** (cnt//2), 4 * (10 ** (cnt//2))
        else : stt, end = 3 * (10 ** (cnt//2)), 10 ** ((cnt//2)+1)

        mid = (stt + end) // 2
        while end - stt > 1 :
            if mid * mid < num :
                stt = mid
                mid = (stt + end) // 2
            else :
                end = mid
                mid = (stt + end) // 2
        
        if stt * stt == num or end * end == num : return True
        else : return False