## https://leetcode.com/problems/convert-a-number-to-hexadecimal/

dics={10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f', 16:'0'}
for i in range(10) : dics[i] = str(i)
nums = 2 ** 31 #16 ** 7    # 2**28

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num < 0 :
            num = nums + num
            ans = ''

            while num // 16 > 0 :
                ans = dics[num % 16] + ans
                num = num // 16
                
            if ans == '' :
                ans = dics[num % 16]
                num = num // 16

            for i in range(7-len(ans)) :
                ans = '0' + ans
            
            ans = dics[(num%16)+8] + ans

        else :
            ans = dics[num % 16]
            while num // 16 > 0 :
                num = num // 16
                ans = dics[num % 16] + ans
        return ans