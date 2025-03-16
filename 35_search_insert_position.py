"""
https://leetcode.com/problems/search-insert-position/description/

Use binary search, but instead of returning -1 when an element is not found, return the 'low' index
used in that iteration.
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)

    def binarySearch(self, nums: List[int], low: int, high: int,target: int) -> int:
        if low > high:
            return low
        midIdx = low + (high - low) // 2
        mid = nums[midIdx]
        if (mid == target):
            return midIdx
        elif target < mid:
            return self.binarySearch(nums, low, midIdx - 1, target)
        else:
            return self.binarySearch(nums, midIdx + 1, high, target)
            