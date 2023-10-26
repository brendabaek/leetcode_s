## https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        idx, ln = 0, len(arr)
        while idx < ln :
            num = arr[idx]
            if num >= 0 :
                for i in range(idx+1, ln) :
                    if num * 2 == arr[i] : return True
                    elif num * 2 < arr[i] : break
            else :
                for i in range(idx-1, -1, -1) :
                    if num * 2 == arr[i] : return True
                    elif num * 2 > arr[i] : break
            idx += 1
        return False