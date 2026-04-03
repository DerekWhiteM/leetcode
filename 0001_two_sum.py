from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            num_needed = target - num
            if num_needed in seen:
                return [seen[num_needed], i]
            else:
                seen[num] = i
        return []    
