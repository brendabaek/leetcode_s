## https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = s.split(" ")
        new_lst, new_word = [], ''
        for l in lst :
            for new_l in l :
                new_word = new_l + new_word
            new_lst.append(new_word)
            new_word = ''
        return ' '.join(new_lst)

        tmp, ans = '', ''
        for l in s :
            if l != ' ' :
                tmp = l + tmp
            else :
                ans = ans + tmp + ' '
                tmp = ''
        return ans + tmp