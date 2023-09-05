## https://leetcode.com/problems/self-dividing-numbers/

lst = []
for i in range(1, (10**4)+1) :
    c, str_num = True, str(i)
    for s in str_num :
        if int(s) == 0 or i % int(s) != 0 :
            c = False
            break
    if c == True : lst.append(i)
        
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for i in lst :
            if left <= i and i <= right : ans.append(i)
        return ans