class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = list(nums)
        nums.sort(reverse=True)
        ln = len(nums)
        ans = []

        for i in range(ln):
            for j in range(i+1, ln):
                if nums[i] + nums[j] == target :
                    if nums[i] == nums[j] :
                        ans.append(idx.index(nums[i]))
                        idx.remove(nums[i])
                        ans.append(idx.index(nums[j])+1)
                    else: 
                        ans.append(idx.index(nums[i]))
                        ans.append(idx.index(nums[j]))
                else :
                    continue
        ans.sort()
        return(ans)