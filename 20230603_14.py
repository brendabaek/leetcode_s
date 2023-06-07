## https://leetcode.com/problems/longest-common-prefix/
    
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ln = len(strs)
        if ln == 1 :
            return strs[0]
        
        strs.sort(key=len)
        lter = strs[0]
        keyln = len(strs[0])
        ans = ""

        for i in range(keyln) :
            pr = lter[0:i+1]

            for j in range(1, ln) :
                if strs[j][0:i+1] == pr :
                    if j == ln-1 : ans = pr
                    else : continue
                else : break
            if ans == pr : continue
            else : break

        return ans