## https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

prime_number = []
for i in range(2, 21) :
    c = True
    for j in range(2, i) :
        if i % j == 0 : c = False
    if c == True : prime_number.append(i)

class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        ans = 0
        for num in range(left, right+1) :
            if bin(num).count('1') in prime_number : ans += 1
        return ans