class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        for i in range(n):
            for j in range(i+1,n):
                area = (j-i)*(min(heights[i],heights[j]))
                if area>maxArea:
                    maxArea = area
        return maxArea
