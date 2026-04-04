from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        running_sum = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]

            # Restart the running sum once it becomes negative.
            # We know it is only going to make the next num smaller.
            if running_sum < 0:
                running_sum = 0

            running_sum += num
            if running_sum > max_sum:
                max_sum = running_sum
        return max_sum
