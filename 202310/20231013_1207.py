## https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        dics = {}
        for a in arr :
            try : dics[a] += 1
            except : dics[a] = 1
        lst = []
        for v in dics.values() : lst.append(v)
        lst.sort()
        idx, ln = 1, len(lst)
        while idx < ln :
            if lst[idx-1] == lst[idx] : return False
            idx += 1
        return True