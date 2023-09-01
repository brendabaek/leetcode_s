## https://leetcode.com/problems/image-smoother/

class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        r, c = len(img), len(img[0])
        ans = [[0 for j in range(c)] for i in range(r)]
        for i in range(r) :
            for j in range(c) :
                cnt, sums = 0, 0
                for m in range(max(0, i-1), min(r, i+2)) :
                    for n in range(max(0, j-1), min(c, j+2)) :
                        sums += img[m][n]
                        cnt += 1
                ans[i][j] = sums/cnt
        return ans