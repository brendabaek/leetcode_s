## https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dics = {"type" : 0, "color" : 1, "name": 2}
        ans, r = 0, dics[ruleKey]
        for item in items :
            if item[r] == ruleValue : ans += 1
        return ans