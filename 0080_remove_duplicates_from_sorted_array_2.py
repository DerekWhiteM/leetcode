"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

Maintain a slow and fast pointer. Swap when fast points to a non-duplicate.
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 2
        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        return slow 
