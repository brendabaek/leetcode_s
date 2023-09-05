## https://leetcode.com/problems/flood-fill/

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        return self.make_answer(image, sr, sc, color, image[sr][sc])
    
    def make_answer(self, image, sr, sc, color, pre) :
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) : return image
        if pre == color : return image
        if image[sr][sc] != pre : return image
        
        image[sr][sc] = color
        self.make_answer(image, sr-1, sc, color, pre)
        self.make_answer(image, sr+1, sc, color, pre)
        self.make_answer(image, sr, sc-1, color, pre)
        self.make_answer(image, sr, sc+1, color, pre)
        return image