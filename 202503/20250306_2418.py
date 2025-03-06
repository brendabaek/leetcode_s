## https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        idx, dics = 0, {}
        for h in heights : dics[idx] = h; idx += 1
        return [names[i] for i in list(sorted(dics, key=dics.get, reverse=True))]