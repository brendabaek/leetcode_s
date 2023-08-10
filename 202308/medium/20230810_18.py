## https://leetcode.com/problems/4sum/

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        lst1, tg_cnt, lst3 = [], 0, []
        if target % 4 == 0 :
            tg = target / 4
            for n in nums :
                if n < tg : lst1.append(n)
                elif n > tg : lst3.append(n)
                else : tg_cnt += 1
                
        else :
            tg = target / 4
            for n in nums :
                if n > tg : lst3.append(n)
                else : lst1.append(n)

        s_lst1 = set(lst1)
        s_lst3 = set(lst3)

        ans = set()
        ln1, ln3 = len(lst1), len(lst3)

        if tg_cnt >= 4 : ans.add(tuple([tg, tg, tg, tg]))

        if ln1 >= 1 and ln3 >= 3 :
            for i in range(ln3-2) :
                for j in range(i+1, ln3-1) :
                    for k in range(j+1, ln3) :
                        if target - (lst3[i] + lst3[j] + lst3[k]) in s_lst1 :
                            ans.add(tuple(sorted([lst3[i], lst3[j], lst3[k], target-(lst3[i] + lst3[j] + lst3[k])])))
        
        if ln1 >= 2 and ln3 >= 2 :
            for i in range(ln1-1) :
                for j in range(i+1, ln1) :
                    for k in range(ln3-1) :
                        for l in range(k+1, ln3) :
                            if target - (lst1[i] + lst1[j]) == lst3[k] + lst3[l] :
                                ans.add(tuple(sorted([lst1[i], lst1[j], lst3[k], lst3[l]])))
        
        if ln1 >= 3 and ln3 >= 1 :
            for i in range(ln1-2) :
                for j in range(i+1, ln1-1) :
                    for k in range(j+1, ln1) :
                        if target - (lst1[i] + lst1[j] + lst1[k]) in s_lst3 :
                            ans.add(tuple(sorted([lst1[i], lst1[j], lst1[k], target-(lst1[i] + lst1[j] + lst1[k])])))

        
        if tg_cnt >= 1 :
            for i in range(ln1-1) :
                for j in range(i+1, ln1) :
                        if target - tg - (lst1[i] + lst1[j]) in s_lst3 :
                            ans.add(tuple(sorted([lst1[i], lst1[j], tg, target-tg-(lst1[i] + lst1[j])])))

            for i in range(ln3-1) :
                for j in range(i+1, ln3) :
                        if target - tg - (lst3[i] + lst3[j]) in s_lst1 :
                            ans.add(tuple(sorted([lst3[i], lst3[j], tg, target-tg-(lst3[i] + lst3[j])])))

        if tg_cnt >= 2 :
            for i in range(ln1) :
                if target - (tg * 2) - lst1[i] in s_lst3 :
                    ans.add(tuple(sorted([lst1[i], tg, tg, target-tg-tg-lst1[i]])))

        return ans