class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0
        while left < right:
            print(heights[left])
            print(heights[right])
            current = min(heights[left], heights[right]) * (right - left)
            area = current if current > area else area
            if heights[left] < heights[right]:
                old_left = left
                left = left + 1
                while left < right and not (heights[left] > heights[old_left]):
                    left = left + 1
            else:
                old_right = right
                right = right - 1
                while left < right and not (heights[right] > heights[old_right]):
                    right = right - 1
        return area