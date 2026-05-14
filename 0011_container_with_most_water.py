from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = (right - left) * min(height[left], height[right])

        for _ in range(len(height) - 1):
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            area = (right - left) * min(height[left], height[right])
            if area > max_area:
                max_area = area

        return max_area
