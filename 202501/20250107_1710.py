## https://leetcode.com/problems/maximum-units-on-a-truck/

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x:x[1], reverse = True)
        ans = 0
        for box in boxTypes :
            if box[0] < truckSize :
                ans += box[0] * box[1]
                truckSize -= box[0]
            elif box[0] > truckSize : return ans + (truckSize * box[1])
            else : return ans + (box[0] * box[1])
        return ans