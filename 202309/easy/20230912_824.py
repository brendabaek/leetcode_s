## https://leetcode.com/problems/goat-latin/

class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        s_lst = sentence.split(' ')
        check = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ln, cnt, ans = len(s_lst), 2, ''
        for i in range(ln) :
            tmp = 'm' + ('a' * (i+2)) + ' '
            if s_lst[i][0] in check : ans += s_lst[i] + tmp
            else : ans += s_lst[i][1:] + s_lst[i][0] + tmp
            cnt += 1
        return ans[:-1]