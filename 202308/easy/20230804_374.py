## https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        stt, mid, end = 1, (1+n)//2, n
        while stt != mid and end != mid :
            if guess(mid) == 0 : return mid
            elif guess(mid) == 1 :
                stt = mid
                mid = (stt+end) // 2
            elif guess(mid) == -1 :
                end = mid
                mid = (stt+end) // 2
        
        if guess(stt) == 0 : return stt
        else : return end