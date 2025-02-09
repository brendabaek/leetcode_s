## https://leetcode.com/problems/kth-distinct-string-in-an-array/

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        lst, d_lst = [], []
        for a in arr :
            if a in d_lst : continue
            elif a in lst :
                lst.remove(a)
                d_lst.append(a)
            else : lst.append(a)
        return lst[k-1] if len(lst) >= k else ""