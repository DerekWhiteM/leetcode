"""
https://leetcode.com/problems/rotate-array

Put the first index into its new spot, then put that index into its new spot, and so on.
"""

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        currentIdx = 0
        holding = None
        length = len(nums)
        for i in range(length + 1):
            currentValue = nums[currentIdx]
            nums[currentIdx] = holding
            if currentValue != None:
                holding = currentValue
                currentIdx = (currentIdx + k) % length
            else:
                nextIdx = (currentIdx + 1) % length
                holding = nums[nextIdx]
                if (i < length):
                    nums[nextIdx] = None
                currentIdx = (currentIdx + k + 1) % length
