class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights)-1

        area = max(0, (r-l) * min(heights[l],heights[r]))
        while l<r:

            if heights[l] <= heights[r]:
                l+=1
                area = max(area, (r-l) * min(heights[l],heights[r]))
            else:
                r-=1
                area = max(area, (r-l) * min(heights[l],heights[r]))
        return area