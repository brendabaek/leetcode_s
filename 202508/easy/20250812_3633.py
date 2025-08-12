## https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        landEndTime, waterEndTime = [], []
        for l1, l2 in zip(landStartTime, landDuration): landEndTime.append(l1 + l2)
        for w1, w2 in zip(waterStartTime, waterDuration): waterEndTime.append(w1 + w2)
        ans, ln1, ln2 = 4000, len(landEndTime), len(waterEndTime)
        for i in range(ln1):
            if landEndTime[i] >= ans: continue
            for j in range(ln2):
                if landEndTime[i] >= waterStartTime[j]: ans = min(ans, landEndTime[i] + waterDuration[j])
                else: ans = min(ans, waterEndTime[j])
        for k in range(ln2):
            if waterEndTime[k] >= ans: continue
            for l in range(ln1):
                if waterEndTime[k] >= landStartTime[l]: ans = min(ans, waterEndTime[k] + landDuration[l])
                else: ans = min(ans, landEndTime[l])
        return ans