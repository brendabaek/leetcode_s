## https://leetcode.com/problems/simplify-path/

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        tmp, lst = [], []
        for t in path.split('/') :
            if t : tmp.append(t)

        for i in range(len(tmp)) :
            if tmp[i] == '.' : pass
            elif tmp[i] == '..' :
                try : lst.pop()
                except : pass
            else : lst.append(tmp[i])
            
        ans = ''
        for l in lst : ans += '/' + l

        if ans == '' : return '/'
        else : return ans