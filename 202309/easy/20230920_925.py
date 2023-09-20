## https://leetcode.com/problems/long-pressed-name/

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        while len(name) > 0 and len(typed) > 0 :
            idx1, idx2 = 0, -1
            pre = name[idx1]
            try :
                while name[idx1+1] == pre : idx1 += 1
            except : pass
            try :
                while typed[idx2+1] == pre : idx2 += 1
            except : pass
            if idx2 == -1 : return False
            if idx1 > idx2 : return False
            name, typed = name[idx1+1:], typed[idx2+1:]
            if name == typed : return True
            elif name == '' and typed != '' : return False
            elif name != '' and typed == '' : return False
        return True