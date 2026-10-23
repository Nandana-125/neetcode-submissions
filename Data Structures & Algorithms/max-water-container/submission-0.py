class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0 
        n = len(heights)
        r = n - 1 
        res = 0 

        while l<r: 
            if heights[l] < heights[r]: 
                h = heights[l]
                b = r-l 
                area = h*b 
                l= l+1 
            else : 
                h = heights[r]
                b = r-l 
                area = h*b 
                r = r-1 

            res = max(area,res)

        return res   

        