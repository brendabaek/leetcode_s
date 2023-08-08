## https://leetcode.com/problems/3sum-closest/

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 3 : return sum(nums)
        
        lst1, tg_cnt, lst3 = [], 0, []

        if target % 3 == 0 :
            tg = target / 3
            for n in nums :
                if n < tg : lst1.append(n)
                elif n > tg : lst3.append(n)
                else :
                    tg_cnt += 1
                    if tg_cnt >= 3 : return target

        else :
            tg = target // 3
            for n in nums :
                if n <= tg : lst1.append(n)
                else : lst3.append(n)

        s_lst1, s_lst3, set_lst = set(lst1), set(lst3), set(lst1+lst3)
        if tg_cnt > 0 :
            for num in s_lst1 :
                if (target-num) in s_lst3 : return target

        if len(lst1) == 0 and len(lst3) != 0 :
            for i in range(tg_cnt) :
                lst3.append(tg)
            lst3.sort()
            ans = lst3[0] + lst3[1] + lst3[2]
            return ans

        elif len(lst1) != 0 and len(lst3) == 0 :
            for i in range(tg_cnt) :
                lst1.append(tg)
            lst1.sort()
            ans = lst1[-1] + lst1[-2] + lst1[-3]
            return ans

        else : # len(lst1) != 0 and len(lst3) != 0 :
            sums = 0
            num1_lst, num3_lst = [], []

            ln1 = len(lst1)
            for c1 in range(ln1-1) :
                for c2 in range(c1+1, ln1) :
                    num1 = target - lst1[c1] - lst1[c2]
                    if num1 in s_lst3 : return target
                    else : num1_lst.append(num1)

            ln3 = len(lst3)
            for c3 in range(ln3-1) :
                for c4 in range(c3+1, ln3) :
                    num3 = target - lst3[c3] - lst3[c4]
                    if num3 in s_lst1 : return target
                    else : num3_lst.append(num3)
            
            cnt = 1
            ans = None
            num1_lst, num3_lst = set(num1_lst), set(num3_lst)
            while ans == None :
                for num1 in num1_lst :
                    if num1 + cnt in set_lst :
                        ans = target + cnt
                    elif num1 - cnt in set_lst :
                        ans = target - cnt
                    if ans != None : return ans
                for num3 in num3_lst :
                    if num3 + cnt in set_lst :
                        ans = target + cnt
                    elif num3 - cnt in set_lst :
                        ans = target - cnt
                    if ans != None : return ans
                cnt += 1
            return ans