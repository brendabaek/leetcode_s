## https://leetcode.com/problems/coupon-code-validator/

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        dics = {"electronics" : [], "grocery" : [], "pharmacy" : [], "restaurant" : []}
        for i in range(len(code)):
            if isActive[i] != True: continue
            if not code[i].replace('_', 'a').isalnum(): continue
            if businessLine[i] in dics: dics[businessLine[i]].append(code[i])
        return [v for value in dics.values() for v in sorted(value)]