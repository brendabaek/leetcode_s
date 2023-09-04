## https://leetcode.com/problems/1-bit-and-2-bit-characters/

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        cnt = 0
        while cnt < len(bits)-1 :
            if bits[cnt] == 1 : cnt += 2
            else : cnt += 1

        if cnt == len(bits) : return False
        else : return bits[-1] == 0