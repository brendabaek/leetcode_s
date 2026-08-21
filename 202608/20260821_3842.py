## https://leetcode.com/problems/toggle-light-bulbs/

class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        lst = []
        bulbs.sort()
        for b in bulbs:
            if lst == [] or lst[-1] != b: lst.append(b)
            else: lst.pop()
        return lst