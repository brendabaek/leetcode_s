## https://leetcode.com/problems/interleaving-string/

# class Solution(object):
#     def isInterleave(self, s1, s2, s3):
#         """
#         :type s1: str
#         :type s2: str
#         :type s3: str
#         :rtype: bool
#         """
#         print("stt", s1, s2, s3)

#         if s1 == '' : return s2 == s3
#         if s2 == '' : return s1 == s3
#         if s3 == '' : return (s1 == '') and (s2 == '')
#         if s1[0] != s3[0] and s2[0] != s3[0] : return False

#         cnt1, cnt2, cnt3, check = 0, 0, 0, True
#         while (s1[cnt1] == s3[cnt1]) and (cnt1 < len(s1)) and (cnt1 < len(s3)) : cnt1 += 1
#         while cnt1 > 0 :
#             if (s2[cnt2] != s3[cnt1+cnt2]) and (cnt2 < len(s2)) and ((cnt1+cnt2) < len(s3)) : cnt1 -= 1
#             if (s2[cnt2] == s3[cnt1+cnt2]) and (cnt2 < len(s2)) and ((cnt1+cnt2) < len(s3)) :
#                 check = self.isInterleave(s1[cnt1:], s2, s3[cnt1:])
#             if 

#             while (s2[cnt2] == s3[cnt1+cnt2]) and (cnt2 < len(s2)) and ((cnt1+cnt2) < len(s3)) : cnt2 += 1
#             if self.isInterleave(s1[cnt1:], s2, s3[cnt1:]) == False : cnt1 -= 1
#             else :
                
#                 while cnt2 > 0 :
#                     if self.isInterleave(s1, s2[cnt2:], s3[(cnt1+cnt2):]) == False : cnt2 -= 1
#                     else : return True
#         return False