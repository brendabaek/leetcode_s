## https://leetcode.com/problems/contains-duplicate-ii/

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums == None or k == None : return False
        dics = {}
        cnt = 0

        for n in nums :
            if n not in dics : dics[n] = [cnt]
            else : dics[n].append(cnt)
            cnt += 1

        for v in dics.values():
            ln = len(v)
            if ln > 1 :
                for i in range(ln-1) :
                    for j in range(i+1, min(ln, i+1+k)) :
                        if v[j] - v[i] <= k : return True

        return False