## https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        dics, set_lst = {}, set()
        for d in deck :
            try : dics[d] += 1
            except : dics[d] = 1
        for v in dics.values() :
            if v == 1 : return False
            set_lst.add(v)
        
        min_num = min(set_lst)
        for m in range(2, min_num+1) :
            ans = True
            if min_num % m == 0 :
                for num in set_lst :
                    if num % m != 0 :
                        ans = False
                        break
            else : ans = False
            if ans == True : return True
        return ans