## https://leetcode.com/problems/score-validator/

class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score, counter = 0, 0
        for e in events:
            if e == "W": counter += 1
            elif e in ["WD", "NB"]: score += 1
            else: score += int(e)
            if counter == 10: break
        return [score, counter]