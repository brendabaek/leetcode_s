## https://leetcode.com/problems/get-maximum-in-generated-array/

lst, m = [0, 1], 0
for idx in range(1, 51) :
    lst.append(lst[idx])
    lst.append(sum(lst[idx:idx+2]))

for i in range(len(lst)) :
    m = max(lst[i], m)
    lst[i] = m

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        return lst[n]