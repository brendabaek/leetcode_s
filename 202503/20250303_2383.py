## https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        if initialEnergy <= sum(energy) : ans = sum(energy) - initialEnergy + 1
        else : ans = 0
        for i in experience :
            if initialExperience <= i :
                ans += i - initialExperience + 1
                initialExperience += i - initialExperience + 1
            initialExperience += i
        return ans