class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 1 :
            return strs[0]
        
        lst1 = [(st, len(st)) for st in strs]
        lst2 = sorted(lst1, key=itemgetter(1))
        lst3 = [i[0] for i in lst2]
        ln = len(lst3)

        lter = lst3[0]
        keyln = len(lter)
        ans = ""

        for i in range(keyln) :
            pr = lter[0:i+1]

            for j in range(1, ln) :
                if lst3[j][0:i+1] == pr :
                    if j == ln-1 : ans = pr
                    else : continue
                else : break
            if ans == pr : continue
            else : break

        return ans