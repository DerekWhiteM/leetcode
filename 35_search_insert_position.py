from typing import List

"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)
        
    def binarySearch(self, nums: List[int], low: int, high: int,target: int) -> int:
        if low == high:
            if target > nums[low]:
                return low + 1
            else:
                return low - 1
        midIdx = low + (high - low) // 2
        mid = nums[midIdx]
        if (mid == target):
            return midIdx
        elif target > mid:
            return self.binarySearch(nums, midIdx + 1, high, target)
        else:
            return self.binarySearch(nums, low, midIdx - 1, target)

solution = Solution() 
print(solution.searchInsert([1, 3, 5, 6], 5)) # -> 2
print(solution.searchInsert([1, 3, 4, 6], 5)) # -> 2
print(solution.searchInsert([1, 3, 5, 6], 0)) # -> 0