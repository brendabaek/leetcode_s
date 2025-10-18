## https://leetcode.com/problems/majority-frequency-characters/

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        d1, d2 = {}, {}
        for i in s:
            try: d1[i] += 1
            except: d1[i] = 1
        for l, cnt in d1.items():
            try: d2[cnt] += l
            except: d2[cnt] = l
        return sorted(d2.items(), key=lambda x: (len(x[1]), x[0]), reverse = True)[0][1]