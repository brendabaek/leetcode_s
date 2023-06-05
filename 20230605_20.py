## https://leetcode.com/problems/valid-parentheses/


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1 : return False
        lst = [i for i in s]
        ans_lst = [['(', ')'], ['{', '}'], ['[', ']']]
        ans = True
        cnt = 0

        while len(lst) > 0 and ans == True :
            ans = False
            for i in range(cnt, len(lst)) :
                if lst[i:i+2] in ans_lst :
                    print(lst[i:i+2])
                    ans = True
                    del lst[i:i+2]
                    cnt = i-1
                    break

        return ans