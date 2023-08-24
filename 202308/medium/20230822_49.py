## https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        disc = {}
        for s in strs :
            new_s = ''.join(sorted(s))
            if new_s in disc : disc[new_s] += [s]
            else : disc[new_s] = [s]
        return [i for i in disc.values()]