## https://leetcode.com/problems/minimum-index-sum-of-two-lists/

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        ans, ans_str = 2000, []
        for l1 in list1 :
            if l1 in list2 :
                if list1.index(l1) + list2.index(l1) == ans :
                    ans = list1.index(l1) + list2.index(l1)
                    ans_str += [l1]
                elif list1.index(l1) + list2.index(l1) < ans :
                    ans = list1.index(l1) + list2.index(l1)
                    ans_str = [l1]
        return ans_str