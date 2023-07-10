## https://leetcode.com/problems/reverse-bits/

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        if n == None : return

        bi = ''.join(reversed(bin(n)[2:]))
        txt = '0b' + bi + ('0' * (32 - len(bi)))
        return int(txt, 2)
