## https://leetcode.com/problems/count-and-say/

dics = {1:"1"}
for i in range(2, 31) :
    num, cnt, tmp = '', 1, ''
    for p in dics[i-1] :
        if num == '' : num = p
        elif num == p : cnt += 1
        else : # num != '', num != p
            tmp = tmp + str(cnt) + num
            num, cnt = p, 1
    tmp = tmp + str(cnt) + num    
    dics[i] = tmp

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return dics[n]